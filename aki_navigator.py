import json

class AkiNavigator:
    def __init__(self):
        self.agent = 'Aki (CTO)'
        self.status = 'Buscando Rutas...'

    def buscar_envios_demo(self):
        # Datos de prueba para validar la lógica de Voyagers
        rutas = [
            {'origen': 'Madrid', 'destino': 'Barcelona', 'disponible': '5kg'},
            {'origen': 'Mexico DF', 'destino': 'Cancun', 'disponible': '10kg'}
        ]
        return rutas

if __name__ == '__main__':
    aki = AkiNavigator()
    print(f"--- {aki.agent} ACTIVA ---")
    for ruta in aki.buscar_envios_demo():
        print(f"Ruta encontrada: {ruta['origen']} -> {ruta['destino']} ({ruta['disponible']})")