import requests
import json
import os
import sys
import compileall

# CONFIGURACIÓN
PORTAL_URL = "http://localhost:3000"
RUTAS_FILE = r"C:\Users\ADMIN\Voyagers-Cloud\portal-web\src\app\rutas.json"
PYTHON_ROOT = r"C:\Users\ADMIN\Voyagers-Cloud\portal-web\src\app"

def test_web_server():
    """Simula a un humano abriendo el navegador."""
    print("👀 [VALENTINA]: Verificando si el Portal Web está vivo...")
    try:
        response = requests.get(PORTAL_URL, timeout=3)
        if response.status_code == 200:
            print("✅ Web operativa (Estado 200 OK).")
            return True
        else:
            print(f"❌ La web responde con error: {response.status_code}")
            return False
    except:
        print("❌ No se puede conectar a localhost:3000. ¿Está apagado el servidor?")
        return False

def test_json_integrity():
    """Simula a un humano revisando que los datos no estén corruptos."""
    print("🧠 [AKI]: Analizando lógica de datos (JSON)...")
    if not os.path.exists(RUTAS_FILE):
        print("⚠️ Archivo de rutas no encontrado (Aún no generado).")
        return True # Pasamos, porque puede ser la primera vez
    
    try:
        with open(RUTAS_FILE, 'r', encoding='utf-8') as f:
            json.load(f)
        print("✅ Estructura de datos VÁLIDA.")
        return True
    except json.JSONDecodeError as e:
        print(f"❌ ERROR CRÍTICO DE DATOS: {e}")
        return False

def test_python_syntax():
    """Simula a un humano compilando el código antes de ejecutar."""
    print("🔧 [LUKAS]: Buscando errores de sintaxis en scripts...")
    try:
        # Intenta compilar todos los .py en la carpeta sin ejecutarlos
        if compileall.compile_dir(PYTHON_ROOT, quiet=1):
            print("✅ Sintaxis de código Python CORRECTA.")
            return True
        else:
            print("❌ Se detectaron errores de sintaxis en el código.")
            return False
    except Exception as e:
        print(f"⚠️ Error al verificar sintaxis: {e}")
        return False

if __name__ == "__main__":
    print("\n🔍 --- INICIANDO PROTOCOLO DE CALIDAD VOYAGERS ---")
    web_ok = test_web_server()
    data_ok = test_json_integrity()
    code_ok = test_python_syntax()
    
    if web_ok and data_ok and code_ok:
        print("\n🚀 [DECISIÓN]: Todo funciona. El equipo autoriza el despliegue.")
        sys.exit(0) # Éxito
    else:
        print("\n🛑 [DECISIÓN]: Se han encontrado fallos. Deteniendo operaciones para auto-reparación.")
        sys.exit(1) # Fallo
