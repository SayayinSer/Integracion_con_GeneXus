import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, ActivatedRoute, RouterModule } from '@angular/router';
import { CajaService } from '../../services/caja.service';
import { Caja } from '../../models/models';

@Component({
  selector: 'app-cajas-form',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './cajas-form.html'
})
export class CajasForm implements OnInit {
  caja: Caja = {
    CajaId: '',
    CajaDescripcion: '',
    CajaEstado: 'A',
    CajaSaldoInicial: 0,
    CajaSaldoActual: 0
  };
  
  loading = false;
  isEdit = false;
  errorMessage = '';

  constructor(
    private cajaService: CajaService,
    private router: Router,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.isEdit = true;
      this.cargarCaja(id);
    }
  }

  cargarCaja(id: string) {
    this.loading = true;
    this.cajaService.getCaja(id).subscribe({
      next: (res) => {
        if (res.SDT) {
          this.caja = res.SDT;
        }
        this.loading = false;
      },
      error: (err) => {
        this.errorMessage = 'Error al cargar la caja.';
        this.loading = false;
        console.error(err);
      }
    });
  }

  guardar() {
    this.loading = true;
    this.errorMessage = '';

    const payload = {
      CajaId: this.caja.CajaId,
      CajaDescripcion: this.caja.CajaDescripcion,
      CajaEstado: this.caja.CajaEstado,
      CajaSaldoInicial: Number(this.caja.CajaSaldoInicial)
    };

    if (this.isEdit && this.caja.CajaId) {
      this.cajaService.actualizarCaja(this.caja.CajaId, payload as any).subscribe({
        next: () => this.router.navigate(['/cajas']),
        error: (err) => {
          this.errorMessage = 'Error al modificar la caja.';
          this.loading = false;
          console.error(err);
        }
      });
    } else {
      this.cajaService.crearCaja(payload as any).subscribe({
        next: () => this.router.navigate(['/cajas']),
        error: (err) => {
          this.errorMessage = 'Error al insertar la caja. Verifique que no exista el mismo ID.';
          this.loading = false;
          console.error(err);
        }
      });
    }
  }
}
