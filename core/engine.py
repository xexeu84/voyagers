import os

class VoyagersCore:
    """
    Núcleo de Lógica de Negocio Voyagers 3.0
    Gestiona la valoración del espacio disponible en diferentes medios de transporte.
    """
    def __init__(self):
        self.team = ["Marcus", "Aki", "Valentina", "Lukas"]
        self.version = "3.0-SPACE-MARKET"
        # Reglas Financieras Inmutables
        self.base_fee = 2.50
        self.commission_pct = 0.15

    def calcular_tarifa_sugerida(self, tipo_transporte, peso_kg, distancia_km):
        """
        Calcula el precio base sugerido dependiendo del medio de transporte.
        El espacio en avión es más caro y rápido que en barco.
        """
        multiplicadores = {
            "avion": 1.5,   # Alta velocidad, alto coste
            "coche": 0.8,   # Economía colaborativa estándar
            "barco": 0.5,   # Lento, barato, gran volumen
            "camion": 0.6   # Logística terrestre
        }
        
        factor = multiplicadores.get(tipo_transporte.lower(), 0.8)
        precio_base = (peso_kg * factor) + (distancia_km * 0.05)
        return round(precio_base, 2)

    def validar_espacio(self, dimensiones_cm, tipo_transporte):
        # Lógica futura para validar si cabe en cabina/maletero
        return True

# Instancia global
core_engine = VoyagersCore()
