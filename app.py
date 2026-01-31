from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Interfaz Adaptativa (Funciona en movil y PC)
HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VOYAGERS - P2P Global</title>
    <style>
        :root { --neon: #00ff41; --bg: #0a0a0a; }
        body { background: var(--bg); color: var(--neon); font-family: sans-serif; margin: 0; display: flex; justify-content: center; }
        .app-container { width: 100%; max-width: 500px; padding: 20px; box-sizing: border-box; }
        .header { border-bottom: 2px solid var(--neon); text-align: center; padding-bottom: 10px; }
        .card { border: 1px solid var(--neon); padding: 15px; margin-top: 20px; border-radius: 8px; background: #111; }
        .btn { background: var(--neon); color: #000; width: 100%; border: none; padding: 15px; font-weight: bold; border-radius: 5px; cursor: pointer; text-transform: uppercase; }
        @media (min-width: 768px) { .app-container { max-width: 800px; } }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="header">
            <h1>VOYAGERS</h1>
            <small>GLOBAL P2P LOGISTICS</small>
        </div>
        <div class="card">
            <h3>VIAJERO: Gana dinero</h3>
            <p>Publica el espacio libre en tu maleta.</p>
            <button class="btn" onclick="alert('Conectando con base de datos de Aki...')">PUBLICAR RUTA</button>
        </div>
        <div class="card">
            <h3>REMITENTE: Ahorra envíos</h3>
            <p>Envía paquetes a través de viajeros verificados.</p>
            <button class="btn" style="background:transparent; color:var(--neon); border: 1px solid var(--neon);">BUSCAR VIAJERO</button>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_LAYOUT)

if __name__ == "__main__":
    # Lukas fuerza el puerto de la nube para acceso externo
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
