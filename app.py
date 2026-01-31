from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import os

app = Flask(__name__)

# Configuración de Base de Datos
def init_db():
    conn = sqlite3.connect('data/voyagers.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS routes 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       origin TEXT, destination TEXT, weight INTEGER, price REAL)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/publish', methods=['POST'])
def publish():
    data = request.form
    conn = sqlite3.connect('data/voyagers.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO routes (origin, destination, weight, price) VALUES (?, ?, ?, ?)",
                   (data['origin'], data['destination'], data['weight'], data['price']))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/api/routes', methods=['GET'])
def get_routes():
    conn = sqlite3.connect('data/voyagers.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM routes")
    routes = cursor.fetchall()
    conn.close()
    return jsonify(routes)

if __name__ == "__main__":
    if not os.path.exists('data'): os.makedirs('data')
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
