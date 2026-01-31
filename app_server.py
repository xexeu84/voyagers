from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open('routes_database.json', 'r') as f:
            rutas = f.readlines()
    except:
        rutas = ["No hay rutas activas aún."]

    return render_template_string("""
    <html>
        <head><title>Voyagers Cloud Portal</title></head>
        <body style="background:#000; color:#fff; font-family:sans-serif; padding:50px;">
            <h1>VOYAGERS LOGISTICS NODE</h1>
            <div style="border:1px solid #333; padding:20px;">
                <h3>Marketplace en Tiempo Real</h3>
                <ul>
                    {% for ruta in rutas %}
                        <li>{{ ruta }}</li>
                    {% endfor %}
                </ul>
            </div>
        </body>
    </html>
    """, rutas=rutas)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
