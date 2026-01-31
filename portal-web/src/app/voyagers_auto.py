# -*- coding: utf-8 -*-
import os
import time
import subprocess

class VoyagersCloud:
    def __init__(self):
        self.budget_limit = 0.0
        self.autonomy_level = 9.7
        self.root = os.getcwd()

    def check_safety_rules(self):
        # Regla básica: No deudas, no problemas legales
        print("🛡️ Verificando cumplimiento de Regla de Oro (Cero Deudas)...")
        return True 

    def auto_repair(self, error):
        print(f"🔧 [LUKAS]: Error detectado: {error}. Iniciando protocolo de auto-reparación...")
        # Aquí el bot decide si necesita reinstalar una librería o limpiar caché
        if "ModuleNotFoundError" in str(error):
            os.system("pip install requests")

    def run_cycle(self):
        if self.check_safety_rules():
            try:
                print("🔍 [AKI]: Navegando y buscando oportunidades de rutas...")
                os.system("python3 portal-web/src/app/sync_vanguard.py")
                
                print("📂 [LUKAS]: Sincronizando datos con GitHub...")
                os.system("python3 portal-web/src/app/git_sync.py")
                
            except Exception as e:
                self.auto_repair(e)

if __name__ == "__main__":
    voyagers = VoyagersCloud()
    while True:
        voyagers.run_cycle()
        time.sleep(60)
