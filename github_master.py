import os
import subprocess
from datetime import datetime

class GitHubVoyager:
    def __init__(self):
        self.team = {
            "Aki": "Navegacion & Descargas",
            "Kai": "Sincronizacion Cloud",
            "Lukas": "Auditoria Legal",
            "Marcus": "Decision Estrategica"
        }

    def ejecutar_mision(self, tarea):
        print(f"[*] {datetime.now()} - Iniciando mision: {tarea}")
        
        # 1. AKI: Simula descarga y lectura de archivos de logistica
        with open("rutas_descargadas.txt", "w") as f:
            f.write("Ruta: MAD-BCN | Peso: 15kg | Usuario: @Traveler_X")
        print("[+] Aki: Archivo de rutas descargado y escrito.")

        # 2. KAI: Sincronizacion con GitHub
        self.push_to_github(tarea)

    def push_to_github(self, msg):
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", f"Voyagers Auto-Mod: {msg}"], check=True)
            subprocess.run(["git", "push"], check=True)
            print(f"[!] Kai: Cambios subidos a GitHub con exito.")
        except Exception as e:
            print(f"[?] Error de Kai: Revisa permisos de Git ({e})")

if __name__ == "__main__":
    v = GitHubVoyager()
    # Ejecutamos comando masivo
    v.ejecutar_mision("Sincronizacion de agentes elite")