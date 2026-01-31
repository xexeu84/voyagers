import json
import time
import random

def simular_captacion():
    # En un entorno real, aquí Aki conectaría APIs de LinkedIn/Directorios
    # Por ahora, Valentina inicia el llenado de la DB con leads perfilados
    prospectos = [
        {"nombre": "Logistica Express SL", "rol": "Transportista", "contacto": "info@logex.com"},
        {"nombre": "Juan Viajero", "rol": "Viajero P2P", "contacto": "juan.v@mail.com"},
        {"nombre": "Importaciones Globales", "rol": "Cliente", "contacto": "ventas@import.es"}
    ]
    
    print("[VALENTINA] Iniciando ciclo de captacion 24/7...")
    for p in prospectos:
        # Aquí se simula la inserción en la base de datos PostgreSQL
        print(f"[REGISTRO] Nuevo prospecto identificado: {p['nombre']} ({p['rol']})")
        time.sleep(2)
    print("[VALENTINA] Ciclo completado. Esperando nueva ventana de búsqueda...")

if __name__ == "__main__":
    simular_captacion()
