import os

class CloudBot:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.environment = "Railway Cloud"

    def status(self):
        return f"Bot {self.name} ({self.role}) operando en {self.environment}."

# Inicializar equipo
marcus = CloudBot("Marcus-CEO", "Estrategia")
aki = CloudBot("Aki-CTO", "Desarrollo")
valentina = CloudBot("Valentina-CMO", "Marketing")
lukas = CloudBot("Lukas-DELTA", "Infraestructura")

print(lukas.status())
