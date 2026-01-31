import os, time, subprocess
def run():
    while True:
        print("[LUKAS] Entorno: NUBE ETERNA. Sincronizando con GitHub...")
        # Lukas ahora ignora C:\Users\ADMIN y usa rutas relativas del contenedor
        subprocess.run(["git", "pull", "origin", "main"])
        time.sleep(300)
if __name__ == "__main__": run()
