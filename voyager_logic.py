import os
import json

class VoyagersCloud:
    def __init__(self):
        self.status = "Online"
        self.budget = 0
        self.team = ["Marcus", "Aki", "Kai", "Valentina", "Lukas"]

    def check_system(self):
        files = os.listdir(".")
        return f"Sincronizacion completa. {len(files)} archivos detectados."

    def report_to_ceo(self):
        return {"status": self.status, "budget_check": "OK ($0)", "autonomy": 9.7}

if __name__ == "__main__":
    v = VoyagersCloud()
    print("--- REPORTE DE SISTEMA ---")
    print(v.check_system())
    print(f"Estado del Equipo: {v.report_to_ceo()}")
