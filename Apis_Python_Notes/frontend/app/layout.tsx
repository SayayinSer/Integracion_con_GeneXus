import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Link from "next/link";
import { LayoutDashboard, Users, Wallet, Tags, MapPin, FileBox } from "lucide-react";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "GeneXus Python Notes - Dashboard",
  description: "Modern CRUD Interface for GeneXus Transactions",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" suppressHydrationWarning>
      <body className={`${inter.className} min-h-screen bg-slate-50 text-slate-900 font-sans flex overflow-hidden`} suppressHydrationWarning>
        
        {/* Sidebar */}
        <aside className="w-72 bg-slate-900 text-slate-300 flex flex-col transition-all duration-300 shadow-2xl shadow-slate-900/50 z-20 relative">
          <div className="absolute inset-0 bg-gradient-to-b from-slate-800/50 to-transparent pointer-events-none"></div>
          <div className="p-6 flex items-center gap-4 border-b border-slate-800/80 relative z-10">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-sky-400 to-sky-600 flex items-center justify-center text-white font-bold shadow-lg shadow-sky-500/30">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
            </div>
            <div>
              <h1 className="text-xl font-bold text-white tracking-tight">Finanzas</h1>
              <p className="text-xs text-sky-400 font-medium tracking-wide uppercase">Python ERP</p>
            </div>
          </div>
          <nav className="flex-1 py-8 px-4 space-y-2 overflow-y-auto relative z-10">
            <Link href="/" className="flex items-center gap-3 px-4 py-3.5 rounded-xl hover:bg-slate-800 hover:text-white transition-all duration-200 group">
              <LayoutDashboard className="h-5 w-5 opacity-70 group-hover:opacity-100 transition-opacity" />
              <span>Dashboard</span>
            </Link>
            <Link href="/clientes" className="flex items-center gap-3 px-4 py-3.5 rounded-xl hover:bg-slate-800 hover:text-white transition-all duration-200 group">
              <Users className="h-5 w-5 opacity-70 group-hover:opacity-100 transition-opacity" />
              <span>Clientes</span>
            </Link>
            <Link href="/caja" className="flex items-center gap-3 px-4 py-3.5 rounded-xl hover:bg-slate-800 hover:text-white transition-all duration-200 group">
              <Wallet className="h-5 w-5 opacity-70 group-hover:opacity-100 transition-opacity" />
              <span>Cajas y Movimientos</span>
            </Link>
            <div className="pt-6 pb-2 px-4">
              <p className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Configuración</p>
            </div>
            <Link href="/zonas" className="flex items-center gap-3 px-4 py-3.5 rounded-xl hover:bg-slate-800 hover:text-white transition-all duration-200 group">
              <MapPin className="h-4 w-4 opacity-70 group-hover:opacity-100 transition-opacity" />
              <span className="text-sm">Zonas</span>
            </Link>
            <Link href="/categorias" className="flex items-center gap-3 px-4 py-3.5 rounded-xl hover:bg-slate-800 hover:text-white transition-all duration-200 group">
              <Tags className="h-4 w-4 opacity-70 group-hover:opacity-100 transition-opacity" />
              <span className="text-sm">Categorías</span>
            </Link>
            <Link href="/conceptos" className="flex items-center gap-3 px-4 py-3.5 rounded-xl hover:bg-slate-800 hover:text-white transition-all duration-200 group">
              <FileBox className="h-4 w-4 opacity-70 group-hover:opacity-100 transition-opacity" />
              <span className="text-sm">Conceptos de Caja</span>
            </Link>
          </nav>
        </aside>

        {/* Main Content */}
        <main className="flex-1 flex flex-col h-screen overflow-hidden bg-slate-50 relative">
          <div className="absolute top-0 inset-x-0 h-96 bg-gradient-to-b from-sky-50/50 to-transparent pointer-events-none"></div>
          
          <header className="h-[72px] flex-shrink-0 bg-white/70 backdrop-blur-xl border-b border-slate-200/60 flex items-center justify-between px-10 shadow-sm z-10 sticky top-0">
            <div className="flex items-center gap-6">
              <span className="text-sm font-medium text-slate-400 bg-slate-100 px-3 py-1.5 rounded-lg border border-slate-200">FastAPI</span>
              <span className="text-sm font-medium text-slate-400 bg-slate-100 px-3 py-1.5 rounded-lg border border-slate-200">Next.js 14</span>
            </div>
            <div className="flex items-center gap-4">
              <div className="flex items-center gap-3 text-right">
                <div>
                  <p className="text-sm font-bold text-slate-800">Admin User</p>
                  <p className="text-xs text-slate-500">administrator</p>
                </div>
                <div className="w-10 h-10 rounded-full bg-slate-200 border-2 border-white shadow-sm flex items-center justify-center text-slate-500 font-bold">
                  A
                </div>
              </div>
            </div>
          </header>
          
          <div className="flex-1 overflow-auto p-10 relative z-0">
            {children}
          </div>
        </main>
      </body>
    </html>
  );
}
