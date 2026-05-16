import psycopg2
conn = psycopg2.connect(dbname="AngularV1DB", user="postgres", password="123456", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
tables = cur.fetchall()
print("Tables:", tables)
for table in tables:
    tname = table[0]
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tname}'")
    cols = [c[0] for c in cur.fetchall()]
    print(f"Table {tname}: {cols}")
conn.close()
