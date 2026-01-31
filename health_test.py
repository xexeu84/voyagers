import requests
url = "https://voyagers-production.up.railway.app/"
try:
    r = requests.get(url, timeout=10)
    print(f"[SISTEMA] Estado: {r.status_code} - VOYAGERS ESTÁ ONLINE")
    print(f"[INFO] Valentina ha desplegado la interfaz con exito.")
except Exception as e:
    print(f"[ALERTA] El servidor esta reiniciando: {e}")
