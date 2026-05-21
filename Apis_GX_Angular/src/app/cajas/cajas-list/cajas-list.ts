import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { CajaService } from '../../services/caja.service';
import { Caja, ApiResponse } from '../../models/models';

@Component({
  selector: 'app-cajas-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './cajas-list.html'
})
export class CajasList implements OnInit {
  cajas: Caja[] = [];
  loading = true;

  constructor(private cajaService: CajaService) {}

  ngOnInit() {
    this.cargarCajas();
  }

  cargarCajas() {
    this.cajaService.getCajas().subscribe({
      next: (res: ApiResponse<Caja[]>) => {
        this.cajas = res.SDT || [];
        this.loading = false;
      },
      error: (err) => {
        console.error('Error al cargar cajas', err);
        this.loading = false;
      }
    });
  }

  eliminar(id: string | undefined) {
    if (!id) return;
    if (confirm('¿Estás seguro de que deseas eliminar esta caja?')) {
      this.cajaService.eliminarCaja(id).subscribe({
        next: () => this.cargarCajas(),
        error: (err) => alert('Hubo un error al eliminar la caja.')
      });
    }
  }
}
