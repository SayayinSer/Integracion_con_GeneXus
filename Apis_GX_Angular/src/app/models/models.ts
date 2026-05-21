export interface Cliente {
  ClienteCodigo?: number;
  ClienteNombre: string;
  ZonaCodigo: number;
  CategoriaCodigo: number;
}

export interface Caja {
  CajaId: string;
  CajaDescripcion: string;
  CajaEstado: string;
  CajaSaldoInicial: number;
  CajaTotalIngresos?: number;
  CajaTotalEgresos?: number;
  CajaSaldoActual?: number;
}

export interface MovimientoCaja {
  MovimientoCajaId?: number;
  CajaId: string;
  MovimientoCajaDescripcion: string;
  MovimientoCajaImporte: number;
  MovimientoCajaTipo: string;
  MovimientoCajaComprobante: string;
}

export interface ApiResponse<T> {
  SDT: T;
  Messages?: any[];
}
