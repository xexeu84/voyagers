from flask import Flask, render_template, os, json
app = Flask(__name__)

def get_stats():
    if os.path.exists("metrics.json"):
        with open("metrics.json", "r") as f: return json.load(f)
    return {"comisiones_totales": 0.0, "envios_totales": 0}

@app.route('/')
def dashboard():
    return render_template('index.html', stats=get_stats())

@app.route('/transportista')
def transportista():
    return render_template('transportista.html')

@app.route('/cliente')
def cliente():
    return render_template('cliente.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
