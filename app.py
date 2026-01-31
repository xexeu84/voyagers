from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = "VOYAGERS_2026_TOTAL_KEY"

@app.route('/')
def index():
    if session.get('ceo_auth'):
        return render_template('dashboard.html')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Acceso Marcus nivel CEO
    if request.form.get('username') == "marcus" and request.form.get('password') == "Voyagers2026!":
        session['ceo_auth'] = True
        return redirect(url_for('index'))
    return "Acceso Denegado"

if __name__ == "__main__":
    # Forzar el puerto que Railway asigna dinámicamente
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
