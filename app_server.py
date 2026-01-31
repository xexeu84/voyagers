import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>VOYAGERS CLOUD: SISTEMA OPERATIVO</h1><p>Estado: Produccion Perpetua</p>"

if __name__ == "__main__":
    # Forzar el puerto que asigne la nube (Railway/Heroku/etc)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
