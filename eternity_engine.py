import time
import sys

class VoyagersEnsemble:
    def __init__(self):
        self.objetivo_logrado = False
        self.fase = "INTELECTUAL"

    def fase_intelectual(self):
        print("[MARCUS] VALIDANDO: Logistica P2P y Marco Legal...")
        time.sleep(2)
        self.fase = "DESARROLLO"

    def fase_desarrollo(self):
        print("[AKI & VALENTINA] CONSTRUYENDO: Portal Cloud y App PWA...")
        time.sleep(2)
        self.fase = "EJECUCION"

    def fase_ejecucion(self):
        print("[LUKAS] DESPLEGANDO: Verificando funcionalidad en la nube...")
        time.sleep(2)
        self.objetivo_logrado = True
        self.fase = "MANTENIMIENTO_ETERNO"

    def mantenimiento_perpetuo(self):
        # Este es el bucle que no termina nunca
        print("[SISTEMA VOYAGERS] SOPORTE ACTIVO: Monitoreando y Actualizando...")
        time.sleep(10) 

    def iniciar_ciclo_eterno(self):
        while True:
            try:
                if not self.objetivo_logrado:
                    if self.fase == "INTELECTUAL": self.fase_intelectual()
                    elif self.fase == "DESARROLLO": self.fase_desarrollo()
                    elif self.fase == "EJECUCION": self.fase_ejecucion()
                else:
                    self.mantenimiento_perpetuo()
                sys.stdout.flush() # Asegura que veamos los prints en el log
            except Exception as e:
                print(f"[ERROR] Reiniciando modulo: {e}")
            time.sleep(1)

if __name__ == "__main__":
    VoyagersEnsemble().iniciar_ciclo_eterno()
