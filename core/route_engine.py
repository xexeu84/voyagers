import math

def calcular_distancia(coord1, coord2):
    # Simulacion de formula Haversine para distancias reales
    return math.sqrt((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2) * 111

def optimizar_matching(viajero_ruta, paquetes_disponibles):
    print(f"[IA-AKI] Analizando {len(paquetes_disponibles)} paquetes para la ruta {viajero_ruta['origen']}->{viajero_ruta['destino']}")
    
    asignados = []
    for paquete in paquetes_disponibles:
        if paquete['peso'] <= viajero_ruta['capacidad_libre']:
            # Calculo de ahorro CO2 (aprox 0.2kg por km comparado con camion dedicado)
            ahorro_co2 = paquete['distancia_km'] * 0.2
            asignados.append({
                "paquete_id": paquete['id'],
                "ahorro_co2_kg": round(ahorro_co2, 2)
            })
            viajero_ruta['capacidad_libre'] -= paquete['peso']
            
    return asignados

# Prueba de concepto inmediata
viajero = {"origen": "Madrid", "destino": "Barcelona", "capacidad_libre": 10}
paquetes = [
    {"id": "P-001", "peso": 2, "distancia_km": 600},
    {"id": "P-002", "peso": 5, "distancia_km": 600}
]

resultado = optimizar_matching(viajero, paquetes)
print(f"[IA-AKI] Matching completado: {resultado}")
