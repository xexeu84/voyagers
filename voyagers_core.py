import time
import sys

class VoyagersEvolution:
    def __init__(self):
        self.fases = ["INTELECTUAL", "DESARROLLO", "EJECUCION"]
        self.estado_actual = 0

    def trabajar(self):
        while True:
            fase = self.fases[self.estado_actual]
            if fase == "INTELECTUAL":
                print("[MARCUS_BOT] Fase Intelectual: Refinando Business Plan...")
                time.sleep(5)
                self.estado_actual = 1
            elif fase == "DESARROLLO":
                print("[AKI & VALENTINA] Fase Desarrollo: Construyendo Portal y App...")
                time.sleep(5)
                self.estado_actual = 2
            elif fase == "EJECUCION":
                self.mantenimiento_eterno()

    def mantenimiento_eterno(self):
        while True:
            print("[EQUIPO VOYAGERS] MANTENIMIENTO PERPETUO: Optimizando sistema...")
            time.sleep(30)

if __name__ == "__main__":
    VoyagersEvolution().trabajar()
