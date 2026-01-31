# -*- coding: utf-8 -*-
import os, subprocess, time

def ejecutor_fisico():
    print("🚀 [LUKAS]: Ejecutando despliegue de App y Marketplace...")
    
    # Comandos reales de sistema
    comandos = [
        "python3 portal-web/src/app/sync_vanguard.py", # Aki extrae rutas
        "python3 portal-web/src/app/git_sync.py"       # Lukas sube a GitHub
    ]
    
    for cmd in comandos:
        try:
            subprocess.run(cmd, shell=True, check=True)
        except Exception as e:
            print(f"❌ Error en {cmd}: {e}")

if __name__ == "__main__":
    # Bucle infinito de ejecución real en la nube
    while True:
        ejecutor_fisico()
        print("⏳ Esperando 60s para siguiente ciclo autónomo...")
        time.sleep(60)
