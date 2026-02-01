import sys
import os
# Forzamos la raíz del proyecto en el PATH
root = r"C:\Users\ADMIN\Voyagers-Cloud"
if root not in sys.path: sys.path.append(root)

try:
    from core.legal.insurance_engine import generar_poliza_seguro
    res = generar_poliza_seguro("MARCUS_CEO", 150)
    print(f"\n✅ MOTOR LOCALIZADO: Poliza {res['id']} activa.")
    print(f"✅ UBICACIÓN: core/legal/insurance_engine.py")
except Exception as e:
    print(f"\n❌ ERROR CRÍTICO: {e}")
    # Mostrar donde está buscando Python
    print(f"PATH: {sys.path}")
