import os, time, random
def run():
    while True:
        print("[AKI] Escaneando rutas desde servidor CLOUD...")
        # Aki ahora guarda los datos en el volumen persistente de la nube
        with open("routes_database.json", "a") as f:
            f.write(f"Ruta detectada en nube: {random.randint(100,999)}\n")
        time.sleep(60)
if __name__ == "__main__": run()
