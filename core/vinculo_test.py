import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.legal.qr_engine import generar_codigo_seguimiento
from core.legal.insurance_engine import generar_poliza_seguro

def test_vinculo():
    print("--- 🛡️ TEST DE VINCULACIÓN OPERATIVA (CORREGIDO) ---")
    token = generar_codigo_seguimiento("TEST_MARCUS_V2")
    seguro = generar_poliza_seguro("TEST_MARCUS_V2", 100)
    if token.startswith("VOY-") and seguro['cobertura'] == 200:
        print(f"  [OK] Vinculación Lógica: PASADA")
    else:
        print("  [FAIL] Error en parámetros."); sys.exit(1)

if __name__ == "__main__":
    test_vinculo()
