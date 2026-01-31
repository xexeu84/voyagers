import json
import time

def orquestar_bots():
    while True:
        with open('core/mission_manifest.json', 'r') as f:
            plan = json.load(f)
        
        print(f"[MASTER] Ejecutando: {plan['meta_global']}")
        # Lógica de asignación: Aki (Dev), Valentina (Marketing), Lukas (Legal/Seguridad)
        # El bot revisa el estado de cada tarea y ejecuta el código correspondiente
        time.sleep(3600) # Ciclo de revision horaria para persistencia 24/7

if __name__ == "__main__":
    orquestar_bots()
