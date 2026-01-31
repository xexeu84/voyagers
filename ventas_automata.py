import random

class ValentinaSales:
    def __init__(self):
        self.estrategias = [
            "Ahorra hasta un 60% en tu envío con Voyagers.",
            "Tu maleta viaja segura con viajeros verificados.",
            "Recupera el costo de tu billete vendiendo tu espacio libre."
        ]

    def generar_copy_ventas(self, ruta, precio):
        # Lógica de Marketing: Crea un mensaje persuasivo
        ganancia_usuario = round(precio * 0.7, 2)
        return (f"🌟 *OPORTUNIDAD DE NEGOCIO*\n\n"
                f"Hemos detectado una ruta en {ruta}.\n"
                f"Si publicamos ahora, puedes ganar: {ganancia_usuario}€\n"
                f"Frase de marketing: {random.choice(self.estrategias)}\n\n"
                f"¿Lanzamos la campaña, Marcus?")

# Integración con el sistema de Aki
if __name__ == "__main__":
    v = ValentinaSales()
    print(v.generar_copy_ventas("Madrid - París", 45))