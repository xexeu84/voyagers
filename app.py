from flask import Flask, render_template_string
import os

app = Flask(__name__)

# El diseño de Valentina inyectado directamente
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VOYAGERS - P2P Logistics</title>
    <style>
        body { background-color: #0a0a0a; color: #00ff41; font-family: 'Courier New', monospace; margin: 0; padding: 20px; }
        .container { border: 1px solid #00ff41; padding: 20px; border-radius: 5px; max-width: 800px; margin: auto; }
        h1 { text-align: center; text-transform: uppercase; letter-spacing: 5px; border-bottom: 2px solid #00ff41; }
        .status-bar { display: flex; justify-content: space-between; margin-bottom: 20px; font-size: 0.8em; }
        .module { background: #111; border-left: 5px solid #00ff41; padding: 15px; margin: 10px 0; }
        .btn { background: #00ff41; color: black; padding: 10px 20px; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 10px; cursor: pointer;}
    </style>
</head>
<body>
    <div class="container">
        <div class="status-bar">
            <span>SISTEMA: ONLINE</span>
            <span>EQUIPO: AKI, VALENTINA, LUKAS, MARCUS</span>
            <span>FASE: EJECUCIÓN</span>
        </div>
        <h1>VOYAGERS P2P</h1>
        <div class="module">
            <h3>[ MERCADO DE EQUIPAJE ]</h3>
            <p>Estado: Buscando rutas disponibles...</p>
            <div id="rutas">Cargando inteligencia de Aki...</div>
        </div>
        <div class="module">
            <h3>[ TU PRÓXIMO VIAJE ]</h3>
            <p>Vende el espacio libre de tu maleta y recupera el costo de tu billete.</p>
            <button class="btn">PUBLICAR ESPACIO</button>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
