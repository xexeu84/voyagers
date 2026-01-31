import os
import subprocess
import datetime

def run_cmd(cmd):
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if proc.returncode == 0:
        print(f">>> [OK] {cmd[:40]}...")
    else:
        print(f">>> [ERROR] {proc.stderr}")

def mass_production():
    print(f"\n--- VOYAGERS OPS: DESPLIEGUE DE NEGOCIO v3.0 ---")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # INTERFAZ DE PRODUCCIÓN MASIVA
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Voyagers | Gestión de Equipaje</title>
        <style>
            body {{ background: #050505; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 20px; }}
            .container {{ max-width: 800px; margin: auto; border: 1px solid #d4af37; padding: 30px; border-radius: 15px; background: #111; box-shadow: 0 0 20px rgba(212, 175, 55, 0.2); }}
            h1 {{ color: #d4af37; text-align: center; border-bottom: 2px solid #d4af37; padding-bottom: 10px; }}
            .module {{ background: #1a1a1a; padding: 15px; margin: 15px 0; border-radius: 8px; border-left: 5px solid #d4af37; }}
            .status {{ color: #00ff41; font-weight: bold; }}
            .btn {{ background: #d4af37; color: black; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>VOYAGERS LOGISTICS HUB</h1>
            <p style="text-align:center;">Operativo: <span class="status">SÍ</span> | Última Sincronización: {timestamp}</p>
            
            <div class="module">
                <h3>✈️ Panel de Viajero (Oferta de Espacio)</h3>
                <p>Configura el peso disponible en tu próximo vuelo/trayecto.</p>
                <input type="number" placeholder="KG disponibles">
                <button class="btn">Publicar Espacio</button>
            </div>

            <div class="module">
                <h3>📦 Panel de Envío (Demanda)</h3>
                <p>Busca viajeros en tu ruta para ahorrar en aduanas y transporte.</p>
                <input type="text" placeholder="Origen"> ➡️ <input type="text" placeholder="Destino">
                <button class="btn">Buscar Ruta</button>
            </div>

            <div class="module" style="border-left-color: #00ff41;">
                <h3>🛡️ Seguridad y Auditoría (Lukas Delta)</h3>
                <p>Todos los envíos están respaldados legalmente por Voyagers.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    # EJECUCIÓN DE TAREAS EN CADENA
    print(">>> [AKI] Sincronizando lógica de negocio...")
    run_cmd("git add index.html voyager_deploy.py .gitignore")
    run_cmd(f'git commit -m "Business Module v3.0: Interfaz de Pesaje y Rutas"')
    run_cmd("git push origin main")
    
    print(f"\n>>> [VALENTINA] Despliegue exitoso. Revisa: https://xexeu84.github.io/voyagers/")

if __name__ == "__main__":
    mass_production()