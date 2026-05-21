"use client";

import Link from "next/link";
import { Users, Wallet, Activity, ArrowRight } from "lucide-react";

export default function DashboardPage() {
  return (
    <div className="space-y-6 max-w-7xl mx-auto">
      {/* Header */}
      <div className="flex items-end justify-between">
        <div>
          <h1 className="text-2xl font-bold text-slate-800 tracking-tight">Dashboard General</h1>
          <p className="text-slate-500 mt-1">Resumen de la actividad financiera y clientes en FastAPI.</p>
        </div>
        <div className="flex items-center gap-3 text-sm font-medium text-slate-500 bg-white px-4 py-2 rounded-xl shadow-sm border border-slate-200">
          <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
          FastAPI Backend Activo
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-3 gap-6">
        {/* Stat Card 1 */}
        <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 flex items-start gap-4 hover:shadow-md transition-shadow">
          <div className="w-12 h-12 rounded-xl bg-sky-50 text-sky-500 flex items-center justify-center shrink-0">
            <Users className="h-6 w-6" />
          </div>
          <div>
            <p className="text-sm font-medium text-slate-500">Total Clientes</p>
            <p className="text-2xl font-bold text-slate-800 mt-1">Directorio</p>
            <Link href="/clientes" className="text-xs font-medium text-sky-500 mt-2 inline-flex items-center gap-1 hover:text-sky-600">
              Gestionar Clientes <ArrowRight className="h-3 w-3" />
            </Link>
          </div>
        </div>

        {/* Stat Card 2 */}
        <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 flex items-start gap-4 hover:shadow-md transition-shadow">
          <div className="w-12 h-12 rounded-xl bg-indigo-50 text-indigo-500 flex items-center justify-center shrink-0">
            <Wallet className="h-6 w-6" />
          </div>
          <div>
            <p className="text-sm font-medium text-slate-500">Cajas Activas</p>
            <p className="text-2xl font-bold text-slate-800 mt-1">Sucursales</p>
            <Link href="/caja" className="text-xs font-medium text-indigo-500 mt-2 inline-flex items-center gap-1 hover:text-indigo-600">
              Control de Cajas <ArrowRight className="h-3 w-3" />
            </Link>
          </div>
        </div>

        {/* Stat Card 3 */}
        <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl shadow-sm border border-slate-700 p-6 flex flex-col justify-between relative overflow-hidden group">
          <div className="absolute right-0 top-0 w-32 h-32 bg-white/5 rounded-bl-full -mr-8 -mt-8 transition-transform group-hover:scale-110"></div>
          <div>
            <p className="text-sm font-medium text-slate-400">Flujo de Fondos</p>
            <p className="text-2xl font-bold text-white mt-1">Movimientos</p>
          </div>
          <Link href="/caja" className="text-xs font-medium text-slate-300 mt-4 inline-flex items-center gap-1 hover:text-white transition-colors relative z-10">
            Ir a registrar ingresos/egresos <ArrowRight className="h-3 w-3" />
          </Link>
        </div>
      </div>

      {/* Banner */}
      <div className="bg-indigo-50 border border-indigo-100 rounded-2xl p-8 flex items-center justify-between mt-8">
        <div className="flex items-center gap-6">
          <div className="w-16 h-16 rounded-2xl bg-white shadow-sm flex items-center justify-center text-indigo-600">
            <Activity className="h-8 w-8" />
          </div>
          <div>
            <h3 className="text-lg font-bold text-indigo-900">Entorno Python FastAPI & Next.js</h3>
            <p className="text-indigo-700 mt-1 max-w-lg">El backend utiliza la arquitectura de <b>FastAPI y SQLModel</b> replicando el comportamiento de GeneXus. El frontend está construido con la estética profesional <b>Slate & Sky Tailwind CSS</b>.</p>
          </div>
        </div>
      </div>
    </div>
  );
}
