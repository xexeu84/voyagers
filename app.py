from flask import Flask, render_template

app = Flask(__name__)

# Datos simulados (Mock Data) para evitar dependencia de DB en esta fase
ESPACIOS_MOCK = [
    {"id": 1, "tipo": "coche", "precio": 15, "trayecto": "Madrid - Valencia", "capacidad": "Maletero Medio (10kg)", "usuario": "Ana P.", "icono": "fa-car"},
    {"id": 2, "tipo": "avion", "precio": 45, "trayecto": "Barcelona - París", "capacidad": "Equipaje Cabina (5kg)", "usuario": "Jean L.", "icono": "fa-plane"},
    {"id": 3, "tipo": "barco", "precio": 80, "trayecto": "Valencia - Ibiza", "capacidad": "Contenedor Compartido (50kg)", "usuario": "Naviera Baleares", "icono": "fa-ship"},
    {"id": 4, "tipo": "camion", "precio": 120, "trayecto": "Bilbao - Madrid", "capacidad": "Palet Europeo (200kg)", "usuario": "Transportes Norte", "icono": "fa-truck"},
    {"id": 5, "tipo": "coche", "precio": 18, "trayecto": "Valencia - Alicante", "capacidad": "Asiento Trasero (8kg)", "usuario": "Marta S.", "icono": "fa-car"},
    {"id": 6, "tipo": "avion", "precio": 30, "trayecto": "Madrid - Lisboa", "capacidad": "Mochila Extra (3kg)", "usuario": "Joao V.", "icono": "fa-plane"}
]

@app.route('/')
def index():
    return render_template('index.html', espacios=ESPACIOS_MOCK)

@app.route('/health')
def health():
    return {"status": "OK", "system": "Voyagers P2P Core"}

if __name__ == '__main__':
    # Configuración segura para desarrollo local
    print("--- 🚀 VOYAGERS SYSTEM ONLINE ---")
    print("--- Accede a: http://127.0.0.1:5000 ---")
    app.run(debug=True, port=5000)