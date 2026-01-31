from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import os

app = Flask(__name__)
app.secret_key = "MASTER_KEY_2026"

@app.route('/')
def index():
    if session.get('logged_in'): return render_template('dashboard.html')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form.get('username') == "Marcus" and request.form.get('password') == "Voyagers2026!":
        session['logged_in'] = True
        return redirect(url_for('index'))
    return "Acceso Denegado"

@app.route('/api/v1/mission_status')
def status():
    return jsonify({"status": "active", "kpis": {"OTIF": "95%", "CO2_Saved": "12%"}})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
