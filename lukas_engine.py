from voyager_bridge import VoyagerBridge
import time

bridge = VoyagerBridge()
def coordinar():
    while True:
        print("[LUKAS] Coordinando comunicación entre Aki y Valentina...")
        # Aquí Lukas valida que los datos de Aki pasen a la App
        time.sleep(30)

if __name__ == "__main__": coordinar()
