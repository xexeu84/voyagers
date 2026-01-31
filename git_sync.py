import subprocess
import time

def auto_sync_github():
    try:
        print("🔄 [AKI]: Sincronizando con la nube de GitHub...")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Voyagers Autonomous Sync: Mercado P2P Actualizado"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✅ [LUKAS]: Persistencia garantizada en GitHub.")
    except Exception as e:
        print(f"⚠️ [ERROR]: Error de sincronización (Verifica el token/permisos): {e}")

if __name__ == "__main__":
    auto_sync_github()
