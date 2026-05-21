import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, ActivatedRoute, RouterModule } from '@angular/router';
import { ClienteService } from '../../services/cliente.service';
import { Cliente } from '../../models/models';

@Component({
  selector: 'app-clientes-form',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './clientes-form.html'
})
export class ClientesForm implements OnInit {
  cliente: Cliente = {
    ClienteNombre: '',
    ZonaCodigo: 1,
    CategoriaCodigo: 1
  };
  
  loading = false;
  isEdit = false;
  errorMessage = '';

  constructor(
    private clienteService: ClienteService,
    private router: Router,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.isEdit = true;
      this.cargarCliente(Number(id));
    }
  }

  cargarCliente(id: number) {
    this.loading = true;
    this.clienteService.getCliente(id).subscribe({
      next: (res) => {
        if (res.SDT) {
          this.cliente = res.SDT;
        }
        this.loading = false;
      },
      error: (err) => {
        this.errorMessage = 'Error al cargar el cliente.';
        this.loading = false;
        console.error(err);
      }
    });
  }

  guardar() {
    this.loading = true;
    this.errorMessage = '';

    const payload = {
      ClienteNombre: this.cliente.ClienteNombre,
      ZonaCodigo: Number(this.cliente.ZonaCodigo),
      CategoriaCodigo: Number(this.cliente.CategoriaCodigo)
    };

    if (this.isEdit && this.cliente.ClienteCodigo) {
      this.clienteService.actualizarCliente(this.cliente.ClienteCodigo, payload as any).subscribe({
        next: (res) => {
          this.router.navigate(['/clientes']);
        },
        error: (err) => {
          this.errorMessage = 'Error al modificar el cliente.';
          this.loading = false;
          console.error(err);
        }
      });
    } else {
      this.clienteService.crearCliente(payload as any).subscribe({
        next: (res) => {
          this.router.navigate(['/clientes']);
        },
        error: (err) => {
          this.errorMessage = 'Error al insertar el cliente. Verifica que ZonaCodigo y CategoriaCodigo existan.';
          this.loading = false;
          console.error(err);
        }
      });
    }
  }
}
