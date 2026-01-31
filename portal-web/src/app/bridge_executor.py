import subprocess
import time
import os

def ejecutar_comando_autonomo(comando):
    """Ejecuta un comando en la terminal de Windows y devuelve el resultado"""
    try:
        proceso = subprocess.Popen(
            comando,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = proceso.communicate()
        return stdout, stderr
    except Exception as e:
        return None, str(e)

if __name__ == "__main__":
    print("🚀 [PUENTE ACTIVADO]: Los bots ahora tienen control de la terminal.")
    print("🤖 Esperando órdenes de Marcus (CEO)...")
    
    # Prueba de Aki: Listar archivos para confirmar conexión
    out, err = ejecutar_comando_autonomo("dir")
    if out:
        print("✅ Conexión con VS Code: OK")