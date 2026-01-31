from flask import Flask, render_template, request, session, redirect, url_for
from core.engine import engine
import os

app = Flask(__name__)
app.secret_key = "VOYAGERS_CLOUD_KEY"

@app.route('/')
def index():
    if 'user' in session:
        # Ejemplo de cálculo de comisión en vivo para el Dashboard
        comision_ejemplo = engine.calcular_comissao(peso=5, distancia=1000)
        return render_template('dashboard.html', user=session['user'], fee=comision_ejemplo)
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    res = engine.area_acesso("Success")
    if res["status"]:
        session['user'] = request.form.get('username')
        return redirect(url_for('index'))
    return "Acesso Recusado"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
