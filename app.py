from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "VOYAGERS_2026_TOTAL_EXECUTION")

@app.route('/')
def index():
    if session.get('marcus_auth'):
        return render_template('dashboard.html')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Credenciales Maestras fijadas para el CEO Marcus
    if request.form.get('username') == "Marcus" and request.form.get('password') == "Voyagers2026!":
        session['marcus_auth'] = True
        return redirect(url_for('index'))
    return "<h1>Acceso Denegado</h1><p>Credenciales de nivel CEO no reconocidas.</p>"

@app.route('/api/v1/metrics')
def metrics():
    # Indicadores críticos de éxito (KPIs) [cite: 108, 109]
    return jsonify({
        "OTIF": "95.2%",
        "Active_Routes": 0,
        "eCMR_Compliance": "Full",
        "CO2_Level": "Monitoring"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
