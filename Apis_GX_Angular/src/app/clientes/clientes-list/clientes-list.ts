import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ClienteService } from '../../services/cliente.service';
import { Cliente, ApiResponse } from '../../models/models';

@Component({
  selector: 'app-clientes-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './clientes-list.html',
  styleUrls: ['./clientes-list.css']
})
export class ClientesList implements OnInit {
  clientes: Cliente[] = [];
  loading = true;

  constructor(private clienteService: ClienteService) {}

  ngOnInit() {
    this.cargarClientes();
  }

  cargarClientes() {
    this.clienteService.getClientes().subscribe({
      next: (res: ApiResponse<Cliente[]>) => {
        this.clientes = res.SDT || [];
        this.loading = false;
      },
      error: (err) => {
        console.error('Error al cargar clientes', err);
        this.loading = false;
      }
    });
  }

  eliminar(id: number | undefined) {
    if (!id) return;
    if (confirm('¿Estás seguro de que deseas eliminar este cliente?')) {
      this.clienteService.eliminarCliente(id).subscribe({
        next: () => {
          this.cargarClientes();
        },
        error: (err) => {
          console.error('Error al eliminar cliente', err);
          alert('Hubo un error al eliminar el cliente de la base de datos GeneXus.');
        }
      });
    }
  }
}
