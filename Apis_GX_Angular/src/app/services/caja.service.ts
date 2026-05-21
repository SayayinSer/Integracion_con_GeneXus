import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Caja } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class CajaService {
  private apiUrl = 'http://localhost/AngularV1/api/cajas';

  constructor(private http: HttpClient) { }

  getCajas(): Observable<any> {
    return this.http.get<any>(this.apiUrl).pipe(
      map(res => ({ SDT: res.CajaListaSDT || res.SDT || [] }))
    );
  }

  getCaja(id: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`).pipe(
      map(res => ({ SDT: res.Caja_SDT || res.SDT }))
    );
  }

  crearCaja(caja: Caja): Observable<any> {
    return this.http.post<any>(this.apiUrl, caja);
  }

  actualizarCaja(id: string, caja: Caja): Observable<any> {
    const payload = { ...caja, CajaId: id };
    return this.http.put<any>(`${this.apiUrl}/${id}`, payload);
  }

  eliminarCaja(id: string): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`);
  }
}
