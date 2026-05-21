import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { MovimientoCajaService } from '../../../services/movimiento-caja.service';
import { CajaService } from '../../../services/caja.service';
import { MovimientoCaja, Caja } from '../../../models/models';

@Component({
  selector: 'app-movimientos-list',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './movimientos-list.html'
})
export class MovimientosList implements OnInit {
  cajaId = '';
  caja: Caja | null = null;
  movimientos: MovimientoCaja[] = [];
  
  nuevoMovimiento: Partial<MovimientoCaja> = {
    MovimientoCajaDescripcion: '',
    MovimientoCajaImporte: null as unknown as number,
    MovimientoCajaTipo: 'I',
    MovimientoCajaComprobante: ''
  };

  loading = true;
  saving = false;

  constructor(
    private movService: MovimientoCajaService,
    private cajaService: CajaService,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    this.cajaId = this.route.snapshot.paramMap.get('cajaId') || '';
    if (this.cajaId) {
      this.cargarCaja();
      this.cargarMovimientos();
    }
  }

  cargarCaja() {
    this.cajaService.getCaja(this.cajaId).subscribe(res => {
      if (res.SDT) this.caja = res.SDT;
    });
  }

  cargarMovimientos() {
    this.loading = true;
    this.movService.getMovimientos(this.cajaId).subscribe({
      next: (res) => {
        this.movimientos = res.SDT || [];
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.loading = false;
      }
    });
  }

  guardar() {
    if (!this.nuevoMovimiento.MovimientoCajaDescripcion || !this.nuevoMovimiento.MovimientoCajaImporte) return;
    this.saving = true;
    this.movService.crearMovimiento(this.cajaId, this.nuevoMovimiento as any).subscribe({
      next: () => {
        this.nuevoMovimiento = { MovimientoCajaDescripcion: '', MovimientoCajaImporte: null as unknown as number, MovimientoCajaTipo: 'I', MovimientoCajaComprobante: '' };
        this.cargarMovimientos();
        this.cargarCaja(); // Actualizar saldos
        this.saving = false;
      },
      error: () => {
        alert('Error al guardar movimiento. Verifique la API.');
        this.saving = false;
      }
    });
  }

  eliminar(id: number | undefined) {
    if (!id) return;
    if (confirm('¿Estás seguro de eliminar este movimiento?')) {
      this.movService.eliminarMovimiento(id).subscribe({
        next: () => {
          this.cargarMovimientos();
          this.cargarCaja();
        },
        error: () => alert('Error al eliminar movimiento.')
      });
    }
  }
}
