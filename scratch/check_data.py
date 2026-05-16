import psycopg2
conn = psycopg2.connect(dbname="AngularV1DB", user="postgres", password="123456", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("SELECT * FROM zona")
print("Zonas:", cur.fetchall())
cur.execute("SELECT * FROM caja")
print("Cajas:", cur.fetchall())
conn.close()
