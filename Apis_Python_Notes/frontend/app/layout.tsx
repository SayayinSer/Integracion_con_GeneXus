import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "GeneXus Python Notes - Dashboard",
  description: "Modern CRUD Interface for GeneXus Transactions",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" suppressHydrationWarning>
      <body className={inter.className} suppressHydrationWarning>
        <nav className="glass" style={{
          position: 'sticky',
          top: 0,
          zIndex: 50,
          padding: '1rem 2rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: '2rem'
        }}>
          <div style={{ fontWeight: 800, fontSize: '1.25rem', color: 'var(--primary)' }}>
            GX NOTES
          </div>
          <div style={{ display: 'flex', gap: '2rem' }}>
            <a href="/">Dashboard</a>
            <a href="/zonas">Zonas</a>
            <a href="/categorias">Categorías</a>
            <a href="/clientes">Clientes</a>
            <a href="/caja">Caja</a>
            <a href="/conceptos">Conceptos</a>
          </div>
        </nav>
        <main className="container">
          {children}
        </main>
      </body>
    </html>
  );
}
