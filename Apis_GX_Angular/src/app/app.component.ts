import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet, RouterModule } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterModule],
  template: `
    <div class="min-h-screen bg-slate-50 text-slate-900 font-sans flex overflow-hidden">
      <!-- Sidebar -->
      <aside class="w-72 bg-slate-900 text-slate-300 flex flex-col transition-all duration-300 shadow-2xl shadow-slate-900/50 z-20 relative">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-800/50 to-transparent pointer-events-none"></div>
        <div class="p-6 flex items-center gap-4 border-b border-slate-800/80 relative z-10">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-sky-400 to-sky-600 flex items-center justify-center text-white font-bold shadow-lg shadow-sky-500/30">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
          </div>
          <div>
            <h1 class="text-xl font-bold text-white tracking-tight">Finanzas</h1>
            <p class="text-xs text-sky-400 font-medium tracking-wide uppercase">GeneXus ERP</p>
          </div>
        </div>
        <nav class="flex-1 py-8 px-4 space-y-2 overflow-y-auto relative z-10">
          <a routerLink="/" [routerLinkActiveOptions]="{exact: true}" class="flex items-center gap-3 px-4 py-3.5 rounded-xl hover:bg-slate-800 hover:text-white transition-all duration-200 group" routerLinkActive="bg-sky-500/15 text-sky-400 font-medium shadow-inner shadow-sky-500/10">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 opacity-70 group-hover:opacity-100 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" /></svg>
            <span>Dashboard</span>
          </a>
          <a routerLink="/clientes" class="flex items-center gap-3 px-4 py-3.5 rounded-xl hover:bg-slate-800 hover:text-white transition-all duration-200 group" routerLinkActive="bg-sky-500/15 text-sky-400 font-medium shadow-inner shadow-sky-500/10">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 opacity-70 group-hover:opacity-100 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" /></svg>
            <span>Clientes</span>
          </a>
          <a routerLink="/cajas" class="flex items-center gap-3 px-4 py-3.5 rounded-xl hover:bg-slate-800 hover:text-white transition-all duration-200 group" routerLinkActive="bg-sky-500/15 text-sky-400 font-medium shadow-inner shadow-sky-500/10">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 opacity-70 group-hover:opacity-100 transition-opacity" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" /></svg>
            <span>Cajas y Movimientos</span>
          </a>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="flex-1 flex flex-col h-screen overflow-hidden bg-slate-50 relative">
        <!-- Abstract bg element -->
        <div class="absolute top-0 inset-x-0 h-96 bg-gradient-to-b from-sky-50/50 to-transparent pointer-events-none"></div>
        
        <header class="h-[72px] flex-shrink-0 bg-white/70 backdrop-blur-xl border-b border-slate-200/60 flex items-center justify-between px-10 shadow-sm z-10 sticky top-0">
          <div class="flex items-center gap-6">
            <span class="text-sm font-medium text-slate-400 bg-slate-100 px-3 py-1.5 rounded-lg border border-slate-200">GeneXus v18</span>
            <span class="text-sm font-medium text-slate-400 bg-slate-100 px-3 py-1.5 rounded-lg border border-slate-200">Angular 18</span>
          </div>
          <div class="flex items-center gap-4">
            <div class="flex items-center gap-3 text-right">
              <div>
                <p class="text-sm font-bold text-slate-800">Admin User</p>
                <p class="text-xs text-slate-500">administrator</p>
              </div>
              <div class="w-10 h-10 rounded-full bg-slate-200 border-2 border-white shadow-sm flex items-center justify-center text-slate-500 font-bold">
                A
              </div>
            </div>
          </div>
        </header>
        
        <div class="flex-1 overflow-auto p-10 relative z-0">
          <router-outlet></router-outlet>
        </div>
      </main>
    </div>
  `
})
export class AppComponent {
  title = 'apis-gx-angular';
}
