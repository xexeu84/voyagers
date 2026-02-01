from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)
DB_PATH = 'rutas.json'

def cargar_rutas():
    try:
        if not os.path.exists(DB_PATH): return []
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            data = f.read()
            return json.loads(data) if data else []
    except: return []

def guardar_ruta(nueva_ruta):
    rutas = cargar_rutas()
    rutas.insert(0, nueva_ruta)
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(rutas, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    return render_template('index.html', rutas=cargar_rutas())

@app.route('/publicar', methods=['POST'])
def publicar():
    nueva = {
        "precio": request.form.get('precio'),
        "trayecto": f"{request.form.get('origen')} - {request.form.get('destino')}",
        "peso": request.form.get('peso'),
        "usuario": "Marcus"
    }
    guardar_ruta(nueva)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
