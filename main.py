# -*- coding: utf-8 -*-
import os
import sys

if __name__ == "__main__":
    print("🛰️ VOYAGERS CLOUD: Iniciando sistema independiente...")
    
    # Buscamos el script en la ruta de la nube
    script_path = "portal-web/src/app/voyagers_auto.py"
    
    if os.path.exists(script_path):
        os.system(f"python3 {script_path}")
    else:
        print(f"❌ Error: No se encuentra {script_path}")