"use client";

import { useEffect, useState } from "react";
import { fetchData, postData } from "../lib/api";
import { ListChecks, PlusCircle, MapPin } from "lucide-react";

export default function ConceptosPage() {
  const [conceptos, setConceptos] = useState<any[]>([]);
  const [zonas, setZonas] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [newName, setNewName] = useState("");
  const [selectedZona, setSelectedZona] = useState<number>(1);

  useEffect(() => {
    loadData();
  }, []);

  async function loadData() {
    setLoading(true);
    try {
      const [conceptosData, zonasData] = await Promise.all([
        fetchData("/conceptos/"),
        fetchData("/zonas/")
      ]);
      setConceptos(conceptosData);
      setZonas(zonasData);
      if (zonasData.length > 0) setSelectedZona(zonasData[0].zonacodigo);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }

  async function handleCreate() {
    if (!newName) return;
    try {
      await postData("/conceptos/", {
        conceptocajanombre: newName,
        zonaid: selectedZona
      });
      setNewName("");
      loadData();
    } catch (e: any) { alert(e.message); }
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      <header>
        <h1 style={{ color: 'var(--primary)', fontSize: '2.5rem', fontWeight: 800 }}>Conceptos de Caja</h1>
        <p className="text-muted">Definición de rubros por zona geográfica.</p>
      </header>

      <div className="card glass" style={{ display: 'flex', flexWrap: 'wrap', gap: '1.5rem', alignItems: 'flex-end', padding: '1.5rem' }}>
        <div style={{ flex: '2 1 300px' }}>
          <label style={{ fontSize: '0.75rem', color: 'var(--primary)', fontWeight: 'bold' }}>NUEVO CONCEPTO</label>
          <input 
            type="text" 
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
            placeholder="Nombre del concepto..."
            style={{ width: '100%', padding: '0.85rem 1rem', marginTop: '0.5rem', borderRadius: 'var(--radius)', border: '1px solid var(--border)', backgroundColor: 'var(--background)', color: 'var(--foreground)' }}
          />
        </div>
        
        <div style={{ flex: '1 1 200px' }}>
          <label style={{ fontSize: '0.75rem', color: 'var(--primary)', fontWeight: 'bold' }}>ZONA ASOCIADA</label>
          <select 
            value={selectedZona}
            onChange={(e) => setSelectedZona(Number(e.target.value))}
            style={{ width: '100%', padding: '0.85rem 1rem', marginTop: '0.5rem', borderRadius: 'var(--radius)', border: '1px solid var(--border)', backgroundColor: 'var(--background)', color: 'var(--foreground)' }}
          >
            {zonas.map(z => <option key={z.zonacodigo} value={z.zonacodigo}>{z.zonanombre}</option>)}
          </select>
        </div>

        <button onClick={handleCreate} className="btn-primary" style={{ padding: '0.85rem 1.5rem' }}>
          <PlusCircle size={18} />
          Añadir
        </button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '1.5rem' }}>
        {conceptos.map((c, idx) => {
          const zona = zonas.find(z => z.zonacodigo === c.zonaid);
          return (
            <div key={idx} className="card" style={{ padding: '1.5rem', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--primary)' }}>
                <ListChecks size={20} />
                <h3 style={{ margin: 0 }}>{c.conceptocajanombre}</h3>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.8rem', opacity: 0.6 }}>
                <MapPin size={14} />
                <span>Zona: {zona?.zonanombre || `ID ${c.zonaid}`}</span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
