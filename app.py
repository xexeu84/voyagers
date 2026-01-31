from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = "VOYAGERS_2026_TOTAL_KEY"

# Base de datos simulada de usuarios (En producción Aki usará GitHub/SQL)
usuarios_db = {"marcus": "Voyagers2026!"}

@app.route('/')
def index():
    if session.get('auth'): return render_template('dashboard.html')
    return render_template('login.html')

@app.route('/register_page')
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    # Lógica de Lukas: Evitar duplicados y asignar rol
    usuarios_db[email] = request.form.get('password')
    session['auth'] = True
    session['user_role'] = request.form.get('role')
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    if user in usuarios_db and usuarios_db[user] == pw:
        session['auth'] = True
        return redirect(url_for('index'))
    return "<h1>Acceso Denegado</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
