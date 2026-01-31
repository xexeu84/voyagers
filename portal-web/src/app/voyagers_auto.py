import sys
import os
import time
import subprocess

ROOT_DIR = r"C:\Users\ADMIN\Voyagers-Cloud"
sys.path.append(ROOT_DIR)

def ejecutar_comando_autonomo(comando):
    venv_python = os.path.join(ROOT_DIR, ".venv", "Scripts", "python.exe")
    python_exe = venv_python if os.path.exists(venv_python) else "python"
    script_path = os.path.join(ROOT_DIR, comando)
    print(f"🚀 Ejecutando: {comando}...")
    return subprocess.run(f"{python_exe} {script_path}", shell=True)

def modo_autonomo_total():
    print('🔍 Aki verificando servicios y navegación web...')
    ejecutar_comando_autonomo('sync_vanguard.py')
    
    print('📂 Lukas sincronizando base de datos en GitHub...')
    ejecutar_comando_autonomo('git_sync.py')

if __name__ == "__main__":
    print("🚀 Sistema Voyagers Autónomo Iniciado (Nivel 9.7/10)")
    while True:
        try:
            modo_autonomo_total()
            print('🥳 Ciclo completado con éxito. Esperando 60s...')
        except Exception as e:
            print(f'⚠️ Error crítico en el ciclo: {e}')
        time.sleep(60)
