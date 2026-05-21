"use client";

import { useEffect, useState, useMemo } from "react";
import { fetchData, postData, deleteData } from "../lib/api";
import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";
import { 
  Trash2, 
  FileText, 
  Search, 
  PlusCircle, 
  ChevronLeft, 
  ChevronRight,
  User,
  Users
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
        ClienteNombre: newName.toUpperCase(),
        ZonaCodigo: selectedZona,
        CategoriaCodigo: selectedCategoria
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
      (c.ClienteNombre || c.clientenombre || "").toLowerCase().includes(searchTerm.toLowerCase()) ||
      (c.ClienteCodigo || c.clientecodigo || "").toString().includes(searchTerm)
    );
  }, [clientes, searchTerm]);

  const totalPages = Math.ceil(filtered.length / pageSize) || 1;
  const paginated = useMemo(() => {
    const start = (currentPage - 1) * pageSize;
    return filtered.slice(start, start + pageSize);
  }, [filtered, currentPage]);

  function exportPDF() {
    const doc = new jsPDF();
    doc.setFontSize(22);
    doc.text("Reporte de Clientes", 14, 22);
    
    const tableData = filtered.map(c => {
       const cod = c.ClienteCodigo || c.clientecodigo;
       const nom = c.ClienteNombre || c.clientenombre;
       const zonCod = c.ZonaCodigo || c.zonacodigo;
       const catCod = c.CategoriaCodigo || c.categoriacodigo;
       return [
         cod, 
         nom,
         zonas.find(z => (z.ZonaCodigo || z.zonacodigo) === zonCod)?.ZonaNombre || 
         zonas.find(z => (z.ZonaCodigo || z.zonacodigo) === zonCod)?.zonanombre || "N/A",
         categorias.find(cat => (cat.CategoriaCodigo || cat.categoriacodigo) === catCod)?.CategoriaNombre || 
         categorias.find(cat => (cat.CategoriaCodigo || cat.categoriacodigo) === catCod)?.categorianombre || "N/A"
       ];
    });

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
    <div className="flex flex-col gap-8 max-w-7xl mx-auto pb-10">
      <header className="flex justify-between items-start">
        <div>
          <h1 className="text-3xl font-bold text-slate-800 tracking-tight">Directorio de Clientes</h1>
          <p className="text-slate-500 mt-1">Gestión integral de clientes, zonas y categorías.</p>
        </div>
        <button onClick={exportPDF} className="bg-white border border-slate-200 hover:border-sky-500 hover:text-sky-600 text-slate-600 px-4 py-2.5 rounded-xl font-medium shadow-sm transition-all flex items-center gap-2">
          <FileText size={18} />
          Exportar PDF
        </button>
      </header>

      {/* Formulario Alta Rápida */}
      <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 flex flex-wrap gap-4 items-end">
        <div className="flex-1 min-w-[250px]">
          <label className="block text-[10px] text-sky-600 font-bold tracking-wider mb-2">ALTA RÁPIDA DE CLIENTE</label>
          <div className="relative">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <User className="h-5 w-5 text-slate-400" />
            </div>
            <input 
              type="text" 
              value={newName}
              onChange={(e) => setNewName(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleCreate()}
              placeholder="Nombre del cliente..."
              className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-sky-500/20 focus:border-sky-500 transition-all text-slate-700"
            />
          </div>
        </div>
        
        <div className="w-full sm:w-48">
          <label className="block text-[10px] text-slate-500 font-bold tracking-wider mb-2">ZONA</label>
          <select 
            value={selectedZona}
            onChange={(e) => setSelectedZona(Number(e.target.value))}
            className="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-sky-500/20 focus:border-sky-500 transition-all text-slate-700 appearance-none"
          >
            {zonas.map(z => <option key={z.ZonaCodigo || z.zonacodigo} value={z.ZonaCodigo || z.zonacodigo}>{z.ZonaNombre || z.zonanombre}</option>)}
          </select>
        </div>

        <div className="w-full sm:w-48">
          <label className="block text-[10px] text-slate-500 font-bold tracking-wider mb-2">CATEGORÍA</label>
          <select 
            value={selectedCategoria}
            onChange={(e) => setSelectedCategoria(Number(e.target.value))}
            className="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-sky-500/20 focus:border-sky-500 transition-all text-slate-700 appearance-none"
          >
            {categorias.map(c => <option key={c.CategoriaCodigo || c.categoriacodigo} value={c.CategoriaCodigo || c.categoriacodigo}>{c.CategoriaNombre || c.categorianombre}</option>)}
          </select>
        </div>

        <button 
          onClick={handleCreate} 
          className="bg-sky-500 hover:bg-sky-600 text-white px-6 py-2.5 rounded-xl font-medium shadow-sm shadow-sky-500/20 transition-all flex items-center gap-2 h-[46px]"
        >
          <PlusCircle size={20} />
          Registrar
        </button>
      </div>

      <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div className="p-4 border-b border-slate-200 bg-slate-50/50 flex items-center gap-3">
          <Search size={20} className="text-slate-400" />
          <input 
            type="text" 
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Buscar por nombre o ID..."
            className="w-full bg-transparent border-none focus:outline-none text-slate-700 placeholder-slate-400"
          />
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 text-xs uppercase tracking-wider">
              <tr>
                <th className="p-4 font-semibold w-24">ID</th>
                <th className="p-4 font-semibold">Nombre del Cliente</th>
                <th className="p-4 font-semibold">Zona</th>
                <th className="p-4 font-semibold">Categoría</th>
                <th className="p-4 font-semibold text-right">Acciones</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {loading ? (
                <tr className="animate-pulse">
                  <td colSpan={5} className="p-8 text-center text-slate-400">
                    <div className="flex items-center justify-center gap-3">
                      <div className="w-5 h-5 rounded-full border-2 border-sky-500 border-t-transparent animate-spin"></div>
                      Cargando datos de clientes...
                    </div>
                  </td>
                </tr>
              ) : paginated.length === 0 ? (
                <tr>
                  <td colSpan={5} className="p-12 text-center text-slate-400">
                    <Users className="mx-auto h-12 w-12 text-slate-200 mb-3" />
                    <p>No se encontraron clientes.</p>
                  </td>
                </tr>
              ) : (
                paginated.map((c) => {
                  const cod = c.ClienteCodigo || c.clientecodigo;
                  const nom = c.ClienteNombre || c.clientenombre;
                  const zonCod = c.ZonaCodigo || c.zonacodigo;
                  const catCod = c.CategoriaCodigo || c.categoriacodigo;
                  
                  return (
                  <tr key={cod} className="hover:bg-slate-50/80 transition-colors group">
                    <td className="p-4 text-slate-500 font-mono text-sm">#{cod}</td>
                    <td className="p-4 font-medium text-slate-800">
                      <div className="flex items-center gap-3">
                        <div className="w-8 h-8 rounded-full bg-sky-100 text-sky-600 flex items-center justify-center font-bold text-xs">
                          {nom.substring(0,2).toUpperCase()}
                        </div>
                        {nom}
                      </div>
                    </td>
                    <td className="p-4 text-slate-600">
                      <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-50 text-indigo-700 border border-indigo-100">
                        {zonas.find(z => (z.ZonaCodigo || z.zonacodigo) === zonCod)?.ZonaNombre || 
                         zonas.find(z => (z.ZonaCodigo || z.zonacodigo) === zonCod)?.zonanombre || `Zona ${zonCod}`}
                      </span>
                    </td>
                    <td className="p-4 text-slate-600">
                      <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-50 text-emerald-700 border border-emerald-100">
                        {categorias.find(cat => (cat.CategoriaCodigo || cat.categoriacodigo) === catCod)?.CategoriaNombre || 
                         categorias.find(cat => (cat.CategoriaCodigo || cat.categoriacodigo) === catCod)?.categorianombre || `Cat ${catCod}`}
                      </span>
                    </td>
                    <td className="p-4 text-right">
                      <div className="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                        <button onClick={() => handleDelete(cod)} className="p-2 text-slate-400 hover:text-rose-500 hover:bg-rose-50 rounded-lg transition-colors">
                          <Trash2 size={16} />
                        </button>
                      </div>
                    </td>
                  </tr>
                )})
              )}
            </tbody>
          </table>
        </div>

        {totalPages > 1 && !loading && (
          <div className="p-4 border-t border-slate-200 bg-slate-50/50 flex items-center justify-between">
            <span className="text-sm text-slate-500">
              Mostrando página <span className="font-medium text-slate-700">{currentPage}</span> de <span className="font-medium text-slate-700">{totalPages}</span>
            </span>
            <div className="flex items-center gap-2">
              <button 
                disabled={currentPage === 1} 
                onClick={() => setCurrentPage(p => p - 1)}
                className="p-2 rounded-lg border border-slate-200 bg-white text-slate-600 hover:bg-slate-50 hover:text-sky-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                <ChevronLeft size={18} />
              </button>
              <button 
                disabled={currentPage === totalPages} 
                onClick={() => setCurrentPage(p => p + 1)}
                className="p-2 rounded-lg border border-slate-200 bg-white text-slate-600 hover:bg-slate-50 hover:text-sky-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                <ChevronRight size={18} />
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
