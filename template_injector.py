# -*- coding: utf-8 -*-
import os

def generar_plantilla_voyagers():
    print("[AKI] Generando estructura base de la App Voyagers...")
    
    # Este es el esqueleto XML que Blogger entiende
    xml_content = """<?xml version="1.0" encoding="UTF-8" ?>
<managed-template>
  <style>
    body { font-family: sans-serif; background: #f4f4f4; }
    .marketplace { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; padding: 20px; }
    .card { background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    .btn-voyager { background: #000; color: #fff; padding: 10px; border: none; width: 100%; cursor: pointer; }
  </style>
  
  <div class='marketplace'>
    <div class='card'>
      <h3>Ruta Activa: Madrid - CDMX</h3>
      <p>Espacio: 5kg disponibles</p>
      <button class='btn-voyager'>Contactar Viajero</button>
    </div>
    </div>
</managed-template>
"""
    with open("VOYAGERS_THEME_V1.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)
    print("[LUKAS] Plantilla compilada en VOYAGERS_THEME_V1.xml")

if __name__ == "__main__":
    generar_plantilla_voyagers()
