import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Cliente } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ClienteService {
  private apiUrl = 'http://localhost/AngularV1/api/clientes';

  constructor(private http: HttpClient) { }

  getClientes(): Observable<any> {
    return this.http.get<any>(this.apiUrl).pipe(
      map(res => ({ SDT: res.ClienteListaSDT || res.SDT || [] }))
    );
  }

  getCliente(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`).pipe(
      map(res => ({ SDT: res.Cliente_SDT || res.SDT }))
    );
  }

  crearCliente(cliente: Cliente): Observable<any> {
    return this.http.post<any>(this.apiUrl, cliente);
  }

  actualizarCliente(id: number, cliente: Cliente): Observable<any> {
    const payload = { ...cliente, ClienteCodigo: id };
    return this.http.put<any>(`${this.apiUrl}/${id}`, payload);
  }

  eliminarCliente(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`);
  }
}
