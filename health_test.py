import requests
import sys

def test_cloud_health():
    url = "https://voyagers-cloud-production.up.railway.app" # Reemplaza con tu URL real si es distinta
    print(f"[AUDITORIA] Testeando conexion con {url}...")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("[OK] El servidor responde correctamente.")
        else:
            print(f"[ERROR] Codigo de estado: {response.status_code}. Revisar Procfile.")
    except Exception as e:
        print(f"[ERROR DE CONEXION] No se pudo alcanzar el servidor: {e}")

if __name__ == "__main__":
    test_cloud_health()
