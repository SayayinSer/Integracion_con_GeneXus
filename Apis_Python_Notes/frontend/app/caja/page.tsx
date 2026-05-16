"use client";

import { useEffect, useState } from "react";
import { fetchData, postData } from "../lib/api";
import { Wallet, ArrowUpCircle, ArrowDownCircle, History, PlusCircle } from "lucide-react";

export default function CajaPage() {
  const [cajas, setCajas] = useState<any[]>([]);
  const [selectedCaja, setSelectedCaja] = useState<any>(null);
  const [movements, setMovements] = useState<any[]>([]);
  const [showModal, setShowModal] = useState(false);
  const [modalType, setModalType] = useState<'I' | 'E'>('I');
  const [loading, setLoading] = useState(true);

  // Form State
  const [amount, setAmount] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    loadCajas();
  }, []);

  async function loadCajas() {
    setLoading(true);
    try {
      const data = await fetchData("/cajas/");
      setCajas(data);
      if (data.length > 0 && !selectedCaja) {
        setSelectedCaja(data[0]);
        loadMovements(data[0].CajaId);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }

  async function loadMovements(cajaId: string) {
    try {
      const data = await fetchData(`/movimientos/caja/${cajaId}`);
      setMovements(data);
    } catch (e) { console.error(e); }
  }

  async function handleAddMovement() {
    if (!amount || !description || !selectedCaja) return;
    try {
      await postData("/movimientos/", {
        CajaId: selectedCaja.CajaId,
        MovimientoCajaDescripcion: description,
        MovimientoCajaImporte: parseFloat(amount),
        MovimientoCajaTipo: modalType
      });
      setShowModal(false);
      setAmount("");
      setDescription("");
      loadCajas(); // To update balance
      loadMovements(selectedCaja.CajaId);
    } catch (e: any) { alert(e.message); }
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <div>
          <h1 style={{ color: 'var(--primary)', fontSize: '2.5rem', fontWeight: 800 }}>Caja Diaria</h1>
          <p className="text-muted">Control financiero y estados de cuenta.</p>
        </div>
        
        <div style={{ display: 'flex', gap: '1.5rem' }}>
          <div className="card glass" style={{ padding: '0.75rem 1.5rem', textAlign: 'center' }}>
            <div style={{ fontSize: '0.7rem', color: 'var(--muted-foreground)', fontWeight: 'bold' }}>SALDO TOTAL</div>
            <div style={{ fontSize: '1.5rem', fontWeight: 800, color: 'var(--primary)' }}>
              ${cajas.reduce((acc, c) => acc + Number(c.CajaSaldoActual), 0).toLocaleString()}
            </div>
          </div>
          <div className="card glass" style={{ padding: '0.75rem 1.5rem', textAlign: 'center', borderBottom: '2px solid #22c55e' }}>
            <div style={{ fontSize: '0.7rem', color: '#22c55e', fontWeight: 'bold' }}>TOTAL INGRESOS</div>
            <div style={{ fontSize: '1.1rem', fontWeight: 700 }}>
              ${cajas.reduce((acc, c) => acc + Number(c.CajaTotalIngresos), 0).toLocaleString()}
            </div>
          </div>
          <div className="card glass" style={{ padding: '0.75rem 1.5rem', textAlign: 'center', borderBottom: '2px solid #ef4444' }}>
            <div style={{ fontSize: '0.7rem', color: '#ef4444', fontWeight: 'bold' }}>TOTAL EGRESOS</div>
            <div style={{ fontSize: '1.1rem', fontWeight: 700 }}>
              ${cajas.reduce((acc, c) => acc + Number(c.CajaTotalEgresos), 0).toLocaleString()}
            </div>
          </div>
        </div>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem' }}>
        {cajas.map(caja => (
          <div 
            key={caja.CajaId} 
            className={`card glass ${selectedCaja?.CajaId === caja.CajaId ? 'active-caja' : ''}`} 
            style={{ 
              padding: '1.5rem', 
              cursor: 'pointer',
              border: selectedCaja?.CajaId === caja.CajaId ? '2px solid var(--primary)' : '1px solid var(--border)'
            }}
            onClick={() => {
              setSelectedCaja(caja);
              loadMovements(caja.CajaId);
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                <Wallet className="text-primary" size={24} />
                <h3 style={{ margin: 0 }}>{caja.CajaDescripcion}</h3>
              </div>
              <span style={{ 
                padding: '0.25rem 0.75rem', 
                borderRadius: '20px', 
                fontSize: '0.75rem', 
                backgroundColor: caja.CajaEstado === 'A' ? 'rgba(34, 197, 94, 0.1)' : 'rgba(239, 68, 68, 0.1)',
                color: caja.CajaEstado === 'A' ? '#22c55e' : '#ef4444'
              }}>
                {caja.CajaEstado === 'A' ? 'ACTIVA' : 'CERRADA'}
              </span>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginTop: '1.5rem' }}>
              <div className="card" style={{ padding: '1rem', backgroundColor: 'rgba(255,255,255,0.02)' }}>
                <label style={{ fontSize: '0.7rem', color: 'var(--muted-foreground)' }}>SALDO ACTUAL</label>
                <div style={{ fontSize: '1.25rem', fontWeight: 700, color: 'var(--primary)' }}>
                  ${Number(caja.CajaSaldoActual).toLocaleString()}
                </div>
              </div>
              <div className="card" style={{ padding: '1rem', backgroundColor: 'rgba(255,255,255,0.02)' }}>
                <label style={{ fontSize: '0.7rem', color: 'var(--muted-foreground)' }}>INICIAL</label>
                <div style={{ fontSize: '1.25rem', fontWeight: 700 }}>
                  ${Number(caja.CajaSaldoInicial).toLocaleString()}
                </div>
              </div>
            </div>

            <div style={{ display: 'flex', gap: '1rem', marginTop: '1.5rem' }}>
              <button 
                onClick={(e) => { e.stopPropagation(); setShowModal(true); setModalType('I'); setSelectedCaja(caja); }}
                className="btn-primary" 
                style={{ flex: 1, backgroundColor: '#22c55e', display: 'flex', alignItems: 'center', gap: '0.5rem', justifyContent: 'center' }}
              >
                <ArrowUpCircle size={18} /> Ingreso
              </button>
              <button 
                onClick={(e) => { e.stopPropagation(); setShowModal(true); setModalType('E'); setSelectedCaja(caja); }}
                className="btn-primary" 
                style={{ flex: 1, backgroundColor: '#ef4444', display: 'flex', alignItems: 'center', gap: '0.5rem', justifyContent: 'center' }}
              >
                <ArrowDownCircle size={18} /> Egreso
              </button>
            </div>
          </div>
        ))}
        {cajas.length === 0 && !loading && (
           <div className="card" style={{ padding: '3rem', textAlign: 'center', gridColumn: '1 / -1' }}>
              <p className="text-muted">No hay cajas configuradas en el sistema.</p>
              <button 
                onClick={async () => {
                  try {
                    await postData("/cajas/", {
                      CajaId: new Date().toISOString().split('T')[0], // YYYY-MM-DD
                      CajaDescripcion: `Caja ${new Date().toLocaleDateString()}`,
                      CajaSaldoInicial: 0,
                      CajaTotalIngresos: 0,
                      CajaTotalEgresos: 0,
                      CajaSaldoActual: 0,
                      CajaEstado: "A"
                    });
                    loadCajas();
                  } catch (e: any) { alert(e.message); }
                }}
                className="btn-primary" 
                style={{ marginTop: '1rem', alignSelf: 'center' }}
              >
                Abrir Caja del Día
              </button>
           </div>
        )}
      </div>

      {selectedCaja && (
        <section style={{ marginTop: '2rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1.5rem' }}>
            <History className="text-primary" size={24} />
            <h2 style={{ margin: 0 }}>Historial de Movimientos: {selectedCaja.CajaDescripcion}</h2>
          </div>

          <div className="card" style={{ padding: 0, overflow: 'hidden' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse' }}>
              <thead style={{ backgroundColor: 'rgba(255,255,255,0.03)' }}>
                <tr style={{ textAlign: 'left', borderBottom: '1px solid var(--border)' }}>
                  <th style={{ padding: '1rem' }}>Descripción</th>
                  <th style={{ padding: '1rem' }}>Tipo</th>
                  <th style={{ padding: '1rem', textAlign: 'right' }}>Importe</th>
                </tr>
              </thead>
              <tbody>
                {movements.map(m => (
                  <tr key={m.MovimientoCajaId} style={{ borderBottom: '1px solid var(--border)' }}>
                    <td style={{ padding: '1rem' }}>{m.MovimientoCajaDescripcion}</td>
                    <td style={{ padding: '1rem' }}>
                      <span style={{ 
                        color: m.MovimientoCajaTipo === 'I' ? '#22c55e' : '#ef4444',
                        fontWeight: 600,
                        fontSize: '0.8rem'
                      }}>
                        {m.MovimientoCajaTipo === 'I' ? 'INGRESO' : 'EGRESO'}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', textAlign: 'right', fontWeight: 700 }}>
                      {m.MovimientoCajaTipo === 'I' ? '+' : '-'} ${Number(m.MovimientoCajaImporte).toLocaleString()}
                    </td>
                  </tr>
                ))}
                {movements.length === 0 && (
                  <tr>
                    <td colSpan={3} style={{ padding: '2rem', textAlign: 'center', color: 'var(--muted-foreground)' }}>
                      No hay movimientos registrados.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </section>
      )}

      {/* Modal */}
      {showModal && (
        <div style={{
          position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
          backgroundColor: 'rgba(0,0,0,0.8)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000,
          backdropFilter: 'blur(4px)'
        }}>
          <div className="card glass" style={{ width: '400px', padding: '2rem', border: `1px solid ${modalType === 'I' ? '#22c55e' : '#ef4444'}` }}>
            <h2 style={{ marginBottom: '1.5rem', color: modalType === 'I' ? '#22c55e' : '#ef4444' }}>
              Nuevo {modalType === 'I' ? 'Ingreso' : 'Egreso'}
            </h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              <div>
                <label style={{ fontSize: '0.8rem', opacity: 0.7 }}>Descripción</label>
                <input 
                  type="text" 
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  placeholder="Ej: Pago de servicio"
                  style={{ width: '100%', padding: '0.75rem', borderRadius: '8px', border: '1px solid var(--border)', backgroundColor: 'var(--background)', color: 'white' }}
                />
              </div>
              <div>
                <label style={{ fontSize: '0.8rem', opacity: 0.7 }}>Importe</label>
                <input 
                  type="number" 
                  value={amount}
                  onChange={(e) => setAmount(e.target.value)}
                  placeholder="0.00"
                  style={{ width: '100%', padding: '0.75rem', borderRadius: '8px', border: '1px solid var(--border)', backgroundColor: 'var(--background)', color: 'white' }}
                />
              </div>
              <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
                <button onClick={() => setShowModal(false)} className="btn-secondary" style={{ flex: 1, padding: '0.75rem', borderRadius: '8px', background: 'var(--secondary)', color: 'white', border: 'none', cursor: 'pointer' }}>Cancelar</button>
                <button 
                  onClick={handleAddMovement} 
                  className="btn-primary" 
                  style={{ flex: 1, backgroundColor: modalType === 'I' ? '#22c55e' : '#ef4444' }}
                >
                  Registrar
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
