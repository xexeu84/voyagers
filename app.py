from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = "MASTER_KEY_VOYAGERS"

@app.route('/')
def index():
    if session.get('ceo_auth'): return render_template('dashboard.html')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form.get('username') == "Marcus" and request.form.get('password') == "Voyagers2026!":
        session['ceo_auth'] = True
        return redirect('/')
    return "Credenciales de nivel CEO no reconocidas."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
