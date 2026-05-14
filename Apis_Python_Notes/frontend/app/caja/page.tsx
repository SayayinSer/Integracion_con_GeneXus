"use client";

import { useEffect, useState } from "react";
import { fetchData, postData } from "../lib/api";
import { Wallet, ArrowUpCircle, ArrowDownCircle, History, PlusCircle } from "lucide-react";

export default function CajaPage() {
  const [cajas, setCajas] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadCajas();
  }, []);

  async function loadCajas() {
    setLoading(true);
    try {
      // Simulating data or fetching from API if implemented
      // For now, let's assume we fetch all cajas
      const data = await fetchData("/cajas/");
      setCajas(data);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      <header>
        <h1 style={{ color: 'var(--primary)', fontSize: '2.5rem', fontWeight: 800 }}>Caja</h1>
        <p className="text-muted">Control financiero y estados de cuenta.</p>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem' }}>
        {cajas.map(caja => (
          <div key={caja.cajaid} className="card glass" style={{ padding: '1.5rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                <Wallet className="text-primary" size={24} />
                <h3 style={{ margin: 0 }}>{caja.cajadescripcion}</h3>
              </div>
              <span style={{ 
                padding: '0.25rem 0.75rem', 
                borderRadius: '20px', 
                fontSize: '0.75rem', 
                backgroundColor: caja.cajaestado === 'A' ? 'rgba(34, 197, 94, 0.1)' : 'rgba(239, 68, 68, 0.1)',
                color: caja.cajaestado === 'A' ? '#22c55e' : '#ef4444'
              }}>
                {caja.cajaestado === 'A' ? 'ACTIVA' : 'CERRADA'}
              </span>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginTop: '1.5rem' }}>
              <div className="card" style={{ padding: '1rem', backgroundColor: 'rgba(255,255,255,0.02)' }}>
                <label style={{ fontSize: '0.7rem', color: 'var(--muted-foreground)' }}>SALDO ACTUAL</label>
                <div style={{ fontSize: '1.25rem', fontWeight: 700, color: 'var(--primary)' }}>
                  ${caja.cajasaldoactual.toLocaleString()}
                </div>
              </div>
              <div className="card" style={{ padding: '1rem', backgroundColor: 'rgba(255,255,255,0.02)' }}>
                <label style={{ fontSize: '0.7rem', color: 'var(--muted-foreground)' }}>INICIAL</label>
                <div style={{ fontSize: '1.25rem', fontWeight: 700 }}>
                  ${caja.cajasaldoinicial.toLocaleString()}
                </div>
              </div>
            </div>

            <div style={{ display: 'flex', gap: '1rem', marginTop: '1.5rem' }}>
              <button className="btn-primary" style={{ flex: 1, backgroundColor: '#22c55e', display: 'flex', alignItems: 'center', gap: '0.5rem', justifyContent: 'center' }}>
                <ArrowUpCircle size={18} /> Ingreso
              </button>
              <button className="btn-primary" style={{ flex: 1, backgroundColor: '#ef4444', display: 'flex', alignItems: 'center', gap: '0.5rem', justifyContent: 'center' }}>
                <ArrowDownCircle size={18} /> Egreso
              </button>
            </div>
          </div>
        ))}
        {cajas.length === 0 && !loading && (
           <div className="card" style={{ padding: '3rem', textAlign: 'center', gridColumn: '1 / -1' }}>
              <p className="text-muted">No hay cajas configuradas en el sistema.</p>
           </div>
        )}
      </div>
    </div>
  );
}
