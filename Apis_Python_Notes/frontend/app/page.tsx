import Link from "next/link";

export default function Home() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      <header>
        <h1 style={{ fontSize: '3rem', fontWeight: 900, background: 'linear-gradient(to right, #0ea5e9, #38bdf8)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
          Dashboard
        </h1>
        <p className="text-muted">Gestión avanzada de Transacciones GeneXus vía FastAPI.</p>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem' }}>
        <div className="card">
          <h3>Zonas</h3>
          <p className="text-muted" style={{ marginBottom: '1.5rem' }}>Administra las zonas geográficas de la aplicación.</p>
          <Link href="/zonas" className="btn-primary" style={{ display: 'inline-block' }}>
            Gestionar Zonas
          </Link>
        </div>

        <div className="card">
          <h3>Categorías</h3>
          <p className="text-muted" style={{ marginBottom: '1.5rem' }}>Organiza y clasifica los conceptos de la caja.</p>
          <Link href="/categorias" className="btn-primary" style={{ display: 'inline-block' }}>
            Gestionar Categorías
          </Link>
        </div>

        <div className="card">
          <h3>Clientes</h3>
          <p className="text-muted" style={{ marginBottom: '1.5rem' }}>Gestión integral de la cartera de clientes.</p>
          <Link href="/clientes" className="btn-primary" style={{ display: 'inline-block' }}>
            Gestionar Clientes
          </Link>
        </div>

        <div className="card">
          <h3>Caja</h3>
          <p className="text-muted" style={{ marginBottom: '1.5rem' }}>Control de ingresos, egresos y saldos.</p>
          <Link href="/caja" className="btn-primary" style={{ display: 'inline-block' }}>
            Ir a Caja
          </Link>
        </div>
      </div>

      <section className="glass" style={{ padding: '2rem', borderRadius: 'var(--radius)', marginTop: '2rem' }}>
        <h2 style={{ color: 'var(--primary)' }}>Estado de la Infraestructura</h2>
        <div style={{ display: 'flex', gap: '2rem', marginTop: '1rem' }}>
          <div>
            <span className="text-muted">Backend:</span> <span style={{ color: '#22c55e' }}>● Online</span>
          </div>
          <div>
            <span className="text-muted">Database:</span> <span style={{ color: '#22c55e' }}>● Connected (AngularV1DB)</span>
          </div>
        </div>
      </section>
    </div>
  );
}
