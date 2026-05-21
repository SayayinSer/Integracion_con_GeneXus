import { Routes } from '@angular/router';
import { ClientesList } from './clientes/clientes-list/clientes-list';
import { ClientesForm } from './clientes/clientes-form/clientes-form';
import { CajasList } from './cajas/cajas-list/cajas-list';
import { CajasForm } from './cajas/cajas-form/cajas-form';
import { MovimientosList } from './cajas/movimientos/movimientos-list/movimientos-list';
import { Dashboard } from './dashboard/dashboard';

export const routes: Routes = [
  { path: '', component: Dashboard },
  { path: 'clientes', component: ClientesList },
  { path: 'clientes/nuevo', component: ClientesForm },
  { path: 'clientes/editar/:id', component: ClientesForm },
  { path: 'cajas', component: CajasList },
  { path: 'cajas/nuevo', component: CajasForm },
  { path: 'cajas/editar/:id', component: CajasForm },
  { path: 'cajas/:cajaId/movimientos', component: MovimientosList },
  { path: '**', redirectTo: '', pathMatch: 'full' }
];
