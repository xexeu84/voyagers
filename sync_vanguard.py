import os
import json
import time

def sync_all():
    # Aki: La base de datos central
    db_path = "rutas_descargadas.txt"
    
    # Si no existe, creamos una de prueba para que no de error
    if not os.path.exists(db_path):
        with open(db_path, "w", encoding="utf-8") as f:
            f.write("RUTA: Madrid - Barcelona | 05 Feb | 15€\n")
            f.write("RUTA: Valencia - Paris | 10 Feb | 45€\n")

    with open(db_path, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        data = [linea.strip() for linea in lineas[-10:]]

    # 1. Sincronizar con PORTAL WEB
    web_json_dir = "portal-web/src/app"
    os.makedirs(web_json_dir, exist_ok=True)
    with open(os.path.join(web_json_dir, "rutas.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # 2. Sincronizar con APP MÓVIL
    app_json_dir = "voyagers-app"
    os.makedirs(app_json_dir, exist_ok=True)
    with open(os.path.join(app_json_dir, "data.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"✅ [{time.strftime('%H:%M:%S')}] SINC: Web y App sincronizadas con éxito.")

if __name__ == "__main__":
    sync_all()