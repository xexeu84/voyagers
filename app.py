from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = "MASTER_KEY_VOYAGERS_2026"

@app.route('/')
def index():
    if session.get('ceo_auth'): return render_template('dashboard.html')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Acceso forzado para el nivel CEO
    user = request.form.get('username')
    pw = request.form.get('password')
    if user == "marcus" and pw == "Voyagers2026!":
        session['ceo_auth'] = True
        return redirect('/')
    return "<h1>Acceso Denegado</h1><p>Credenciales CEO no validas.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
