import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { MovimientoCaja } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class MovimientoCajaService {
  private apiUrl = 'http://localhost/AngularV1/api/movimientos';

  constructor(private http: HttpClient) { }

  getMovimientos(cajaId: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}?CajaId=${cajaId}`).pipe(
      map(res => ({ SDT: res.MovimientoCajaListaSDT || res.SDT || [] }))
    );
  }

  crearMovimiento(cajaId: string, mov: MovimientoCaja): Observable<any> {
    const payload = { ...mov, CajaId: cajaId };
    return this.http.post<any>(this.apiUrl, payload);
  }

  eliminarMovimiento(movId: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${movId}`);
  }
}
