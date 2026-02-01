from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DB_PATH = 'rutas.json'

def cargar_rutas():
    if not os.path.exists(DB_PATH): return []
    with open(DB_PATH, 'r') as f: return json.load(f)

def guardar_ruta(nueva_ruta):
    rutas = cargar_rutas()
    rutas.insert(0, nueva_ruta)
    with open(DB_PATH, 'w') as f: json.dump(rutas, f)

@app.route('/')
def index():
    rutas = cargar_rutas()
    # Si no hay rutas, Aki mete datos de ejemplo
    if not rutas:
        rutas = [{"precio": "15.00", "trayecto": "Madrid - Barcelona", "peso": "5kg", "usuario": "Marcus"}]
    return render_template('index.html', rutas=rutas)

if __name__ == '__main__':
    app.run(debug=True)
