"use client";

import { useEffect, useState } from "react";
import { fetchData, postData, deleteData } from "../lib/api";
import { Wallet, ArrowUpCircle, ArrowDownCircle, History, PlusCircle, Trash2 } from "lucide-react";

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
      } else if (selectedCaja) {
        // Update selected caja if exists
        const updated = data.find((c: any) => c.CajaId === selectedCaja.CajaId);
        if (updated) setSelectedCaja(updated);
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

  async function handleDeleteMovement(id: number) {
    if (!confirm("¿Eliminar este movimiento y recalcular saldos?")) return;
    try {
      await deleteData(`/movimientos/${id}`);
      loadCajas();
      loadMovements(selectedCaja.CajaId);
    } catch (e: any) { alert(e.message); }
  }

  return (
    <div className="flex flex-col gap-8 max-w-7xl mx-auto pb-10">
      <header className="flex justify-between items-start">
        <div>
          <h1 className="text-3xl font-bold text-slate-800 tracking-tight">Caja Diaria</h1>
          <p className="text-slate-500 mt-1">Control financiero y estados de cuenta.</p>
        </div>
        
        <div className="flex gap-4">
          <div className="bg-white rounded-2xl shadow-sm border border-slate-200 px-6 py-3 text-center min-w-[150px]">
            <div className="text-[10px] text-slate-400 font-bold tracking-wider mb-1">SALDO TOTAL</div>
            <div className="text-2xl font-bold text-slate-800">
              ${cajas.reduce((acc, c) => acc + Number(c.CajaSaldoActual), 0).toLocaleString()}
            </div>
          </div>
          <div className="bg-white rounded-2xl shadow-sm border border-slate-200 px-6 py-3 text-center min-w-[150px] border-b-4 border-b-emerald-500">
            <div className="text-[10px] text-emerald-500 font-bold tracking-wider mb-1">TOTAL INGRESOS</div>
            <div className="text-xl font-bold text-slate-700">
              ${cajas.reduce((acc, c) => acc + Number(c.CajaTotalIngresos), 0).toLocaleString()}
            </div>
          </div>
          <div className="bg-white rounded-2xl shadow-sm border border-slate-200 px-6 py-3 text-center min-w-[150px] border-b-4 border-b-rose-500">
            <div className="text-[10px] text-rose-500 font-bold tracking-wider mb-1">TOTAL EGRESOS</div>
            <div className="text-xl font-bold text-slate-700">
              ${cajas.reduce((acc, c) => acc + Number(c.CajaTotalEgresos), 0).toLocaleString()}
            </div>
          </div>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {cajas.map(caja => (
          <div 
            key={caja.CajaId} 
            className={`bg-white rounded-2xl p-6 cursor-pointer transition-all ${selectedCaja?.CajaId === caja.CajaId ? 'ring-2 ring-sky-500 shadow-md scale-[1.02]' : 'border border-slate-200 shadow-sm hover:shadow-md'}`}
            onClick={() => {
              setSelectedCaja(caja);
              loadMovements(caja.CajaId);
            }}
          >
            <div className="flex justify-between items-center mb-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-sky-50 text-sky-500 flex items-center justify-center">
                  <Wallet size={20} />
                </div>
                <h3 className="font-bold text-slate-800">{caja.CajaDescripcion}</h3>
              </div>
              <span className={`px-3 py-1 rounded-full text-xs font-semibold ${caja.CajaEstado === 'A' ? 'bg-emerald-50 text-emerald-600' : 'bg-rose-50 text-rose-600'}`}>
                {caja.CajaEstado === 'A' ? 'ACTIVA' : 'CERRADA'}
              </span>
            </div>

            <div className="grid grid-cols-2 gap-4 mt-6">
              <div className="bg-slate-50 rounded-xl p-3 border border-slate-100">
                <label className="text-[10px] font-bold text-slate-400">SALDO ACTUAL</label>
                <div className="text-xl font-bold text-sky-600">
                  ${Number(caja.CajaSaldoActual).toLocaleString()}
                </div>
              </div>
              <div className="bg-slate-50 rounded-xl p-3 border border-slate-100">
                <label className="text-[10px] font-bold text-slate-400">INICIAL</label>
                <div className="text-xl font-bold text-slate-700">
                  ${Number(caja.CajaSaldoInicial).toLocaleString()}
                </div>
              </div>
            </div>

            <div className="flex gap-3 mt-6">
              <button 
                onClick={(e) => { e.stopPropagation(); setShowModal(true); setModalType('I'); setSelectedCaja(caja); }}
                className="flex-1 bg-emerald-500 hover:bg-emerald-600 text-white py-2.5 rounded-xl font-medium text-sm flex items-center justify-center gap-2 transition-colors shadow-sm shadow-emerald-500/20"
              >
                <ArrowUpCircle size={18} /> Ingreso
              </button>
              <button 
                onClick={(e) => { e.stopPropagation(); setShowModal(true); setModalType('E'); setSelectedCaja(caja); }}
                className="flex-1 bg-rose-500 hover:bg-rose-600 text-white py-2.5 rounded-xl font-medium text-sm flex items-center justify-center gap-2 transition-colors shadow-sm shadow-rose-500/20"
              >
                <ArrowDownCircle size={18} /> Egreso
              </button>
            </div>
          </div>
        ))}

        {cajas.length === 0 && !loading && (
           <div className="col-span-full bg-white rounded-2xl border border-slate-200 shadow-sm p-12 text-center">
              <p className="text-slate-500 mb-6">No hay cajas configuradas en el sistema.</p>
              <button 
                onClick={async () => {
                  try {
                    await postData("/cajas/", {
                      CajaId: new Date().toISOString().split('T')[0],
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
                className="bg-sky-500 hover:bg-sky-600 text-white px-6 py-3 rounded-xl font-medium shadow-sm shadow-sky-500/20 transition-all inline-flex items-center gap-2"
              >
                <PlusCircle size={20} />
                Abrir Caja del Día
              </button>
           </div>
        )}
      </div>

      {selectedCaja && (
        <section className="mt-4 bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
          <div className="p-6 border-b border-slate-200 bg-slate-50/50 flex items-center gap-3">
            <History className="text-slate-400" size={24} />
            <h2 className="text-lg font-bold text-slate-800 m-0">Historial de Movimientos: {selectedCaja.CajaDescripcion}</h2>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead className="bg-slate-50 text-xs text-slate-500 font-semibold border-b border-slate-200">
                <tr>
                  <th className="p-4 uppercase tracking-wider">Descripción</th>
                  <th className="p-4 uppercase tracking-wider">Tipo</th>
                  <th className="p-4 text-right uppercase tracking-wider">Importe</th>
                  <th className="p-4 text-right uppercase tracking-wider">Acciones</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {movements.map(m => (
                  <tr key={m.MovimientoCajaId} className="hover:bg-slate-50/50 transition-colors group">
                    <td className="p-4 text-slate-700 font-medium">{m.MovimientoCajaDescripcion}</td>
                    <td className="p-4">
                      <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold ${m.MovimientoCajaTipo === 'I' ? 'bg-emerald-50 text-emerald-700 border border-emerald-100' : 'bg-rose-50 text-rose-700 border border-rose-100'}`}>
                        {m.MovimientoCajaTipo === 'I' ? 'INGRESO' : 'EGRESO'}
                      </span>
                    </td>
                    <td className={`p-4 text-right font-bold ${m.MovimientoCajaTipo === 'I' ? 'text-emerald-600' : 'text-rose-600'}`}>
                      {m.MovimientoCajaTipo === 'I' ? '+' : '-'} ${Number(m.MovimientoCajaImporte).toLocaleString()}
                    </td>
                    <td className="p-4 text-right">
                      <button 
                        onClick={() => handleDeleteMovement(m.MovimientoCajaId)} 
                        className="p-2 text-slate-400 hover:text-rose-500 hover:bg-rose-50 rounded-lg transition-colors opacity-0 group-hover:opacity-100"
                      >
                        <Trash2 size={16} />
                      </button>
                    </td>
                  </tr>
                ))}
                {movements.length === 0 && (
                  <tr>
                    <td colSpan={4} className="p-8 text-center text-slate-400">
                      No hay movimientos registrados.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </section>
      )}

      {/* Modal Tailwind */}
      {showModal && (
        <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden border border-slate-200">
            <div className={`p-6 border-b ${modalType === 'I' ? 'border-emerald-100 bg-emerald-50/50' : 'border-rose-100 bg-rose-50/50'}`}>
              <h2 className={`text-xl font-bold m-0 ${modalType === 'I' ? 'text-emerald-700' : 'text-rose-700'}`}>
                Nuevo {modalType === 'I' ? 'Ingreso' : 'Egreso'}
              </h2>
            </div>
            
            <div className="p-6 space-y-5">
              <div>
                <label className="block text-sm font-semibold text-slate-700 mb-1.5">Descripción</label>
                <input 
                  type="text" 
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  placeholder="Ej: Pago de servicio"
                  className="w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-sky-500/20 focus:border-sky-500 transition-all text-slate-700"
                />
              </div>
              <div>
                <label className="block text-sm font-semibold text-slate-700 mb-1.5">Importe ($)</label>
                <input 
                  type="number" 
                  value={amount}
                  onChange={(e) => setAmount(e.target.value)}
                  placeholder="0.00"
                  className="w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-sky-500/20 focus:border-sky-500 transition-all text-slate-700 font-bold"
                />
              </div>
              
              <div className="flex gap-3 pt-4">
                <button 
                  onClick={() => setShowModal(false)} 
                  className="flex-1 px-4 py-3 rounded-xl font-medium bg-slate-100 text-slate-700 hover:bg-slate-200 transition-colors"
                >
                  Cancelar
                </button>
                <button 
                  onClick={handleAddMovement} 
                  className={`flex-1 px-4 py-3 rounded-xl font-medium text-white transition-colors shadow-sm ${modalType === 'I' ? 'bg-emerald-500 hover:bg-emerald-600 shadow-emerald-500/20' : 'bg-rose-500 hover:bg-rose-600 shadow-rose-500/20'}`}
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
