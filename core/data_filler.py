import json
import sqlite3 # O la conexion que usemos en produccion

leads = [
    ("TransEuropa P2P", "Transportista", "info@transeuropa.com"),
    ("Carlos R.", "Viajero", "carlos.p2p@mail.com"),
    ("EcoEnvío Courier", "Transportista", "contacto@ecoenvio.es"),
    ("Marta G.", "Viajero", "marta.g@webmail.com"),
    ("LogisTech Solutions", "Transportista", "ops@logistech.com")
]

print("[VALENTINA] Inyectando leads en la base de datos central...")
# Aqui el bot Aki conectaria con la DB real para persistencia
for nombre, rol, mail in leads:
    print(f"[OK] Registrado: {nombre} como {rol}")
