import os
import json
import random

def simular_crecimiento(n_operaciones):
    archivo = "metrics.json"
    rutas = ["MAD-BCN", "PAR-LON", "NYC-MIA", "BER-FRA"]
    
    if os.path.exists(archivo):
        with open(archivo, "r") as f: data = json.load(f)
    else:
        data = {"comisiones_totales": 0.0, "envios_totales": 0, "ahorro_usuarios": 0.0}
    
    for _ in range(n_operaciones):
        kilos = random.randint(2, 10)
        pago_total = kilos * 12.0 # Tarifa Express
        comision = pago_total * 0.25 # Margen Voyagers
        
        data["comisiones_totales"] += comision
        data["envios_totales"] += 1
        data["ahorro_usuarios"] += (pago_total * 0.4) # Ahorro estimado vs logística tradicional

    with open(archivo, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"✅ Simulación completada: {n_operaciones} envíos procesados.")
    print(f"📊 Nuevo balance de comisiones: {data['comisiones_totales']} EUR")

if __name__ == "__main__":
    simular_crecimiento(10)
