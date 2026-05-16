import requests
import json

base_url = "http://localhost:8000/api/v1"

# 1. Create Caja
caja_res = requests.post(f"{base_url}/cajas/", json={
    "cajadescripcion": "CAJA TEST",
    "cajasaldoinicial": 0,
    "cajatotalingresos": 0,
    "cajatotalegresos": 0,
    "cajasaldoactual": 0,
    "cajaestado": "A"
})
caja = caja_res.json()
print("Caja Created:", caja)
caja_id = caja["cajaid"]

# 2. Create Movement
mov_res = requests.post(f"{base_url}/movimientos/", json={
    "cajaid": caja_id,
    "movimientocajadescripcion": "DEPÓSITO INICIAL",
    "movimientocajaimporte": 1000.0,
    "movimientocajatipo": "I"
})
print("Movement Created:", mov_res.json())

# 3. Check updated balance
caja_final_res = requests.get(f"{base_url}/cajas/")
print("Final Caja State:", caja_final_res.json())
