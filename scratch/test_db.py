import psycopg2
try:
    conn = psycopg2.connect(
        dbname="AngularV1DB",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )
    print("Connection successful")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
