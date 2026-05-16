"use client";

import { useEffect, useState, useMemo } from "react";
import { fetchData, postData, deleteData } from "../lib/api";
import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";
import { 
  Pencil, 
  Trash2, 
  FileText, 
  Search, 
  PlusCircle, 
  ChevronLeft, 
  ChevronRight,
  User
} from "lucide-react";

export default function ClientesPage() {
  const [clientes, setClientes] = useState<any[]>([]);
  const [newName, setNewName] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [zonas, setZonas] = useState<any[]>([]);
  const [categorias, setCategorias] = useState<any[]>([]);
  const [selectedZona, setSelectedZona] = useState<number>(1);
  const [selectedCategoria, setSelectedCategoria] = useState<number>(1);
  const [loading, setLoading] = useState(true);
  
  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 10;

  useEffect(() => {
    loadInitialData();
  }, []);

  async function loadInitialData() {
    setLoading(true);
    try {
      const [clientesData, zonasData, categoriasData] = await Promise.all([
        fetchData("/clientes/"),
        fetchData("/zonas/"),
        fetchData("/categorias/")
      ]);
      setClientes(clientesData);
      setZonas(zonasData);
      setCategorias(categoriasData);
      if (zonasData.length > 0) setSelectedZona(zonasData[0].zonacodigo);
      if (categoriasData.length > 0) setSelectedCategoria(categoriasData[0].categoriacodigo);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }

  async function loadClientes() {
    try {
      const data = await fetchData("/clientes/");
      setClientes(data);
    } catch (e) { console.error(e); }
  }

  async function handleCreate() {
    if (!newName) return;
    try {
      await postData("/clientes/", { 
        clientenombre: newName.toUpperCase(),
        zonacodigo: selectedZona,
        categoriacodigo: selectedCategoria
      });
      setNewName("");
      loadClientes();
    } catch (e: any) { alert(e.message); }
  }

  async function handleDelete(id: number) {
    if (!confirm("¿Eliminar cliente?")) return;
    try {
      await deleteData(`/clientes/${id}`);
      loadClientes();
    } catch (e: any) { alert(e.message); }
  }

  const filtered = useMemo(() => {
    return clientes.filter(c => 
      c.clientenombre.toLowerCase().includes(searchTerm.toLowerCase()) ||
      c.clientecodigo.toString().includes(searchTerm)
    );
  }, [clientes, searchTerm]);

  const totalPages = Math.ceil(filtered.length / pageSize);
  const paginated = useMemo(() => {
    const start = (currentPage - 1) * pageSize;
    return filtered.slice(start, start + pageSize);
  }, [filtered, currentPage]);

  function exportPDF() {
    const doc = new jsPDF();
    doc.setFontSize(22);
    doc.text("Reporte de Clientes", 14, 22);
    
    const tableData = filtered.map(c => [
      c.clientecodigo, 
      c.clientenombre,
      zonas.find(z => z.zonacodigo === c.zonacodigo)?.zonanombre || "N/A",
      categorias.find(cat => cat.categoriacodigo === c.categoriacodigo)?.categorianombre || "N/A"
    ]);

    autoTable(doc, {
      startY: 30,
      head: [['Código', 'Nombre', 'Zona', 'Categoría']],
      body: tableData,
      headStyles: { fillColor: [15, 23, 42] },
      alternateRowStyles: { fillColor: [245, 247, 250] }
    });
    window.open(doc.output("bloburl"), "_blank");
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1 style={{ color: 'var(--primary)', fontSize: '2.5rem', fontWeight: 800 }}>Clientes</h1>
        <button onClick={exportPDF} className="btn-primary" style={{ backgroundColor: '#ef4444' }}>
          <FileText size={18} />
          Reporte PDF
        </button>
      </header>

      <div className="card glass" style={{ display: 'flex', flexWrap: 'wrap', gap: '1.5rem', alignItems: 'flex-end', padding: '1.5rem' }}>
        <div style={{ flex: '2 1 300px' }}>
          <label style={{ fontSize: '0.75rem', color: 'var(--primary)', fontWeight: 'bold' }}>ALTA DE CLIENTE</label>
          <input 
            type="text" 
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleCreate()}
            placeholder="Nombre del cliente..."
            style={{ width: '100%', padding: '0.85rem 1rem', marginTop: '0.5rem', borderRadius: 'var(--radius)', border: '1px solid var(--border)', backgroundColor: 'var(--background)', color: 'var(--foreground)' }}
          />
        </div>
        
        <div style={{ flex: '1 1 150px' }}>
          <label style={{ fontSize: '0.75rem', color: 'var(--primary)', fontWeight: 'bold' }}>ZONA</label>
          <select 
            value={selectedZona}
            onChange={(e) => setSelectedZona(Number(e.target.value))}
            style={{ width: '100%', padding: '0.85rem 1rem', marginTop: '0.5rem', borderRadius: 'var(--radius)', border: '1px solid var(--border)', backgroundColor: 'var(--background)', color: 'var(--foreground)' }}
          >
            {zonas.map(z => <option key={z.zonacodigo} value={z.zonacodigo}>{z.zonanombre}</option>)}
          </select>
        </div>

        <div style={{ flex: '1 1 150px' }}>
          <label style={{ fontSize: '0.75rem', color: 'var(--primary)', fontWeight: 'bold' }}>CATEGORÍA</label>
          <select 
            value={selectedCategoria}
            onChange={(e) => setSelectedCategoria(Number(e.target.value))}
            style={{ width: '100%', padding: '0.85rem 1rem', marginTop: '0.5rem', borderRadius: 'var(--radius)', border: '1px solid var(--border)', backgroundColor: 'var(--background)', color: 'var(--foreground)' }}
          >
            {categorias.map(c => <option key={c.categoriacodigo} value={c.categoriacodigo}>{c.categorianombre}</option>)}
          </select>
        </div>

        <button onClick={handleCreate} className="btn-primary" style={{ padding: '0.85rem 1.5rem' }}>
          <PlusCircle size={18} />
          Registrar
        </button>
      </div>

      <div className="card" style={{ padding: '0.5rem 1rem', display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
        <Search size={20} style={{ color: 'var(--muted-foreground)' }} />
        <input 
          type="text" 
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Buscar clientes..."
          style={{ width: '100%', padding: '0.5rem 0', border: 'none', backgroundColor: 'transparent', color: 'var(--foreground)', outline: 'none' }}
        />
      </div>

      <div className="card" style={{ padding: 0, overflow: 'hidden' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead style={{ backgroundColor: 'rgba(255,255,255,0.03)' }}>
            <tr style={{ textAlign: 'left', borderBottom: '1px solid var(--border)' }}>
              <th style={{ padding: '1.25rem 1rem' }}>ID</th>
              <th style={{ padding: '1.25rem 1rem' }}>Nombre</th>
              <th style={{ padding: '1.25rem 1rem' }}>Zona</th>
              <th style={{ padding: '1.25rem 1rem' }}>Categoría</th>
              <th style={{ padding: '1.25rem 1rem', textAlign: 'right' }}>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {paginated.map((c) => (
              <tr key={c.clientecodigo} className="table-row" style={{ borderBottom: '1px solid var(--border)' }}>
                <td style={{ padding: '1rem' }}>#{c.clientecodigo.toString().padStart(4, '0')}</td>
                <td style={{ padding: '1rem' }}>{c.clientenombre}</td>
                <td style={{ padding: '1rem' }}>
                   <span style={{ fontSize: '0.8rem', opacity: 0.8 }}>
                     {zonas.find(z => z.zonacodigo === c.zonacodigo)?.zonanombre || 'N/A'}
                   </span>
                </td>
                <td style={{ padding: '1rem' }}>
                   <span style={{ fontSize: '0.8rem', opacity: 0.8 }}>
                     {categorias.find(cat => cat.categoriacodigo === c.categoriacodigo)?.categorianombre || 'N/A'}
                   </span>
                </td>
                <td style={{ padding: '1rem', textAlign: 'right' }}>
                  <button onClick={() => handleDelete(c.clientecodigo)} style={{ padding: '0.5rem', borderRadius: '6px', backgroundColor: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', border: 'none' }}>
                    <Trash2 size={18} />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {totalPages > 1 && (
          <div style={{ padding: '1.25rem', display: 'flex', justifyContent: 'center', gap: '1rem' }}>
            <button disabled={currentPage === 1} onClick={() => setCurrentPage(p => p - 1)}><ChevronLeft /></button>
            <span>{currentPage} / {totalPages}</span>
            <button disabled={currentPage === totalPages} onClick={() => setCurrentPage(p => p + 1)}><ChevronRight /></button>
          </div>
        )}
      </div>
    </div>
  );
}
