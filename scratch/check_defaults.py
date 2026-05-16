import psycopg2
conn = psycopg2.connect(dbname="AngularV1DB", user="postgres", password="123456", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("SELECT column_default FROM information_schema.columns WHERE table_name = 'caja' AND column_name = 'cajaid'")
print("Caja ID default:", cur.fetchone())
cur.execute("SELECT column_default FROM information_schema.columns WHERE table_name = 'zona' AND column_name = 'zonacodigo'")
print("Zona ID default:", cur.fetchone())
conn.close()
