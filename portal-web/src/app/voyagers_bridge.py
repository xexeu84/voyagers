import os
import subprocess
import time

def ejecutar_orden_bot(comando, bot_name):
    print(f"🤖 [{bot_name}]: Ejecutando en terminal -> {comando}")
    try:
        # Esto abre un proceso real en tu terminal de Windows
        result = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Éxito: {result.stdout[:50]}...")
        else:
            print(f"❌ Error en terminal: {result.stderr[:50]}...")
    except Exception as e:
        print(f"❓ Fallo crítico de conexión: {e}")

if __name__ == "__main__":
    print("🚀 PUENTE VOYAGERS ACTIVADO - Esperando señales de los bots...")
    # Prueba inicial de Aki para verificar el puente
    ejecutar_orden_bot("python --version", "AKI")