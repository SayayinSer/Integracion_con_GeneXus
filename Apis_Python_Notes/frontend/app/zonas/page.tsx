"use client";

import { useEffect, useState, useMemo } from "react";
import { fetchData, postData, deleteData, putData } from "../lib/api";
import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";
import { 
  Pencil, 
  Trash2, 
  Save, 
  X, 
  FileText, 
  Search, 
  PlusCircle, 
  ChevronLeft, 
  ChevronRight 
} from "lucide-react";

export default function ZonasPage() {
  const [zonas, setZonas] = useState<any[]>([]);
  const [newZona, setNewZona] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [editingId, setEditingId] = useState<number | null>(null);
  const [editValue, setEditValue] = useState("");
  const [loading, setLoading] = useState(true);
  
  // Paginado
  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 10;

  useEffect(() => {
    loadZonas();
  }, []);

  async function loadZonas() {
    setLoading(true);
    try {
      const data = await fetchData("/zonas/");
      setZonas(data);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }

  function validate(value: string) {
    if (!value || value.trim().length === 0) return "El nombre no puede estar vacío.";
    return null;
  }

  async function handleCreate() {
    const validationError = validate(newZona);
    if (validationError) { alert(validationError); return; }
    try {
      await postData("/zonas/", { zonanombre: newZona.toUpperCase() });
      setNewZona("");
      loadZonas();
    } catch (e: any) { alert(e.message); }
  }

  async function handleUpdate(id: number) {
    const validationError = validate(editValue);
    if (validationError) { alert(validationError); return; }
    try {
      await putData(`/zonas/${id}`, { zonanombre: editValue.toUpperCase() });
      setEditingId(null);
      loadZonas();
    } catch (e: any) { alert(e.message); }
  }

  async function handleDelete(id: number) {
    if (!confirm("¿Borrar registro?")) return;
    try {
      await deleteData(`/zonas/${id}`);
      loadZonas();
    } catch (e: any) { alert(e.message); }
  }

  const filteredZonas = useMemo(() => {
    return zonas.filter(z => 
      z.zonanombre.toLowerCase().includes(searchTerm.toLowerCase()) ||
      z.zonacodigo.toString().includes(searchTerm)
    );
  }, [zonas, searchTerm]);

  const totalPages = Math.ceil(filteredZonas.length / pageSize);
  const paginatedZonas = useMemo(() => {
    const start = (currentPage - 1) * pageSize;
    return filteredZonas.slice(start, start + pageSize);
  }, [filteredZonas, currentPage]);

  useEffect(() => {
    setCurrentPage(1);
  }, [searchTerm]);

  function exportPDF() {
    const doc = new jsPDF();
    doc.setFontSize(22);
    doc.setTextColor(15, 23, 42);
    doc.text("Zonas", 14, 22);
    const tableData = filteredZonas.map(z => [z.zonacodigo, z.zonanombre]);
    autoTable(doc, {
      startY: 30,
      head: [['Código', 'Descripción']],
      body: tableData,
      headStyles: { fillColor: [15, 23, 42] },
    });
    const blob = doc.output("bloburl");
    window.open(blob, "_blank");
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1 style={{ color: 'var(--primary)', fontSize: '2.5rem', fontWeight: 800 }}>Zonas</h1>
        <button 
          onClick={exportPDF} 
          className="btn-primary" 
          style={{ backgroundColor: '#ef4444', display: 'flex', alignItems: 'center', gap: '0.5rem' }}
        >
          <FileText size={18} />
          PDF Report
        </button>
      </header>

      {/* Panel de Alta */}
      <div className="card glass" style={{ display: 'flex', gap: '1rem', alignItems: 'center', padding: '1.5rem' }}>
        <div style={{ flex: 1 }}>
          <label style={{ fontSize: '0.75rem', color: 'var(--primary)', fontWeight: 'bold', letterSpacing: '0.05em' }}>NUEVO REGISTRO</label>
          <div style={{ position: 'relative', marginTop: '0.5rem' }}>
            <input 
              type="text" 
              value={newZona}
              onChange={(e) => setNewZona(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleCreate()}
              placeholder="Nombre de la zona..."
              style={{ width: '100%', padding: '0.85rem 1rem', borderRadius: 'var(--radius)', border: '1px solid var(--border)', backgroundColor: 'var(--background)', color: 'var(--foreground)' }}
            />
          </div>
        </div>
        <button 
          onClick={handleCreate} 
          className="btn-primary" 
          style={{ alignSelf: 'flex-end', padding: '0.85rem 1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}
        >
          <PlusCircle size={18} />
          Confirmar
        </button>
      </div>

      {/* Filtro con Icono */}
      <div className="card" style={{ padding: '0.5rem 1rem', display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
        <Search size={20} style={{ color: 'var(--muted-foreground)' }} />
        <input 
          type="text" 
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Buscar registros..."
          style={{ width: '100%', padding: '0.5rem 0', border: 'none', backgroundColor: 'transparent', color: 'var(--foreground)', outline: 'none', fontSize: '1rem' }}
        />
      </div>

      {/* Tabla Premium */}
      <div className="card" style={{ padding: 0, overflow: 'hidden' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead style={{ backgroundColor: 'rgba(255,255,255,0.03)' }}>
            <tr style={{ textAlign: 'left', borderBottom: '1px solid var(--border)' }}>
              <th style={{ padding: '1.25rem 1rem', fontSize: '0.85rem', color: 'var(--muted-foreground)', textTransform: 'uppercase' }}>Código</th>
              <th style={{ padding: '1.25rem 1rem', fontSize: '0.85rem', color: 'var(--muted-foreground)', textTransform: 'uppercase' }}>Descripción</th>
              <th style={{ padding: '1.25rem 1rem', textAlign: 'right', fontSize: '0.85rem', color: 'var(--muted-foreground)', textTransform: 'uppercase' }}>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {paginatedZonas.map((zona) => (
              <tr key={zona.zonacodigo} className="table-row" style={{ borderBottom: '1px solid var(--border)', transition: 'background 0.2s' }}>
                <td style={{ padding: '1rem' }}>
                   <code style={{ color: 'var(--primary)', fontWeight: 600 }}>{zona.zonacodigo.toString().padStart(4, '0')}</code>
                </td>
                <td style={{ padding: '1rem' }}>
                  {editingId === zona.zonacodigo ? (
                    <input 
                      type="text" 
                      value={editValue} 
                      onChange={(e) => setEditValue(e.target.value)} 
                      autoFocus 
                      style={{ padding: '0.5rem', width: '100%', borderRadius: '4px', border: '1px solid var(--primary)', backgroundColor: 'var(--background)', color: 'var(--foreground)' }} 
                    />
                  ) : (
                    <span style={{ fontWeight: 500 }}>{zona.zonanombre}</span>
                  )}
                </td>
                <td style={{ padding: '1rem', textAlign: 'right' }}>
                  <div style={{ display: 'flex', gap: '0.5rem', justifyContent: 'flex-end' }}>
                    {editingId === zona.zonacodigo ? (
                      <>
                        <button 
                          onClick={() => handleUpdate(zona.zonacodigo)} 
                          title="Grabar"
                          style={{ padding: '0.5rem', borderRadius: '6px', backgroundColor: 'rgba(34, 197, 94, 0.1)', color: '#22c55e', border: 'none', cursor: 'pointer' }}
                        >
                          <Save size={18} />
                        </button>
                        <button 
                          onClick={() => setEditingId(null)} 
                          title="Cancelar"
                          style={{ padding: '0.5rem', borderRadius: '6px', backgroundColor: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', border: 'none', cursor: 'pointer' }}
                        >
                          <X size={18} />
                        </button>
                      </>
                    ) : (
                      <>
                        <button 
                          onClick={() => { setEditingId(zona.zonacodigo); setEditValue(zona.zonanombre); }} 
                          title="Modificar"
                          style={{ padding: '0.5rem', borderRadius: '6px', backgroundColor: 'rgba(14, 165, 233, 0.1)', color: 'var(--accent)', border: 'none', cursor: 'pointer' }}
                        >
                          <Pencil size={18} />
                        </button>
                        <button 
                          onClick={() => handleDelete(zona.zonacodigo)} 
                          title="Borrar"
                          style={{ padding: '0.5rem', borderRadius: '6px', backgroundColor: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', border: 'none', cursor: 'pointer' }}
                        >
                          <Trash2 size={18} />
                        </button>
                      </>
                    )}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* Paginado Premium */}
        {totalPages > 1 && (
          <div style={{ padding: '1.25rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', backgroundColor: 'rgba(255,255,255,0.01)' }}>
            <div style={{ fontSize: '0.85rem', color: 'var(--muted-foreground)' }}>
              Mostrando {paginatedZonas.length} de {filteredZonas.length} registros
            </div>
            <div style={{ display: 'flex', gap: '0.5rem' }}>
              <button 
                disabled={currentPage === 1} 
                onClick={() => setCurrentPage(p => p - 1)}
                style={{ padding: '0.5rem', borderRadius: '6px', border: '1px solid var(--border)', cursor: 'pointer', opacity: currentPage === 1 ? 0.3 : 1, backgroundColor: 'var(--background)' }}
              >
                <ChevronLeft size={20} />
              </button>
              <div style={{ display: 'flex', alignItems: 'center', padding: '0 1rem', fontSize: '0.9rem', fontWeight: 600 }}>
                {currentPage} / {totalPages}
              </div>
              <button 
                disabled={currentPage === totalPages} 
                onClick={() => setCurrentPage(p => p + 1)}
                style={{ padding: '0.5rem', borderRadius: '6px', border: '1px solid var(--border)', cursor: 'pointer', opacity: currentPage === totalPages ? 0.3 : 1, backgroundColor: 'var(--background)' }}
              >
                <ChevronRight size={20} />
              </button>
            </div>
          </div>
        )}
      </div>
      
      <style jsx>{`
        .table-row:hover {
          background-color: rgba(255,255,255,0.02);
        }
      `}</style>
    </div>
  );
}
