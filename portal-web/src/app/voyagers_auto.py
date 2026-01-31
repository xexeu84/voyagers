# -*- coding: utf-8 -*-
import sys
import os
import time
import subprocess

# Configuración de rutas para entorno Linux/Cloud
ROOT_DIR = os.getcwd()

def ejecutar_comando_autonomo(comando):
    # En la nube usamos 'python3' directamente
    script_path = os.path.join(ROOT_DIR, comando)
    print(f"--- Ejecutando: {comando} ---")
    return subprocess.run(f"python3 {script_path}", shell=True)

def modo_autonomo_total():
    print('Verificando servicios...')
    ejecutar_comando_autonomo('sync_vanguard.py')
    
    print('Sincronizando base de datos...')
    ejecutar_comando_autonomo('git_sync.py')

if __name__ == "__main__":
    print("🚀 Voyagers Cloud Engine Online")
    while True:
        try:
            modo_autonomo_total()
            print('Ciclo completado. Esperando 60s...')
        except Exception as e:
            print(f'Error: {e}')
        time.sleep(60)
