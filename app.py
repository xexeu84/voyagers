from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Leer métricas reales para el Dashboard
    if os.path.exists("metrics.json"):
        with open("metrics.json", "r") as f:
            stats = json.load(f)
    else:
        stats = {"comisiones_totales": 0.0, "envios_totales": 0}
        
    return render_template('index.html', stats=stats)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
