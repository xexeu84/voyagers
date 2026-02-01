import sys
import os
sys.path.append(os.path.abspath('core'))
from legal.qr_engine import generar_codigo_seguimiento
from legal.insurance_engine import generar_poliza_seguro

def test_vinculo():
    print("--- 🛡️ TEST DE VINCULACIÓN OPERATIVA ---")
    # Simular la acción del botón
    token = generar_codigo_seguimiento("ACCION_BOTON_MARCUS")
    seguro = generar_poliza_seguro("ACCION_BOTON_MARCUS", 250)
    
    if token and seguro['cobertura'] > 0:
        print(f"  [OK] Vinculación exitosa. QR: {token} | Seguro: {seguro['id']}")
    else:
        print("  [FAIL] La vinculación ha fallado."); sys.exit(1)

if __name__ == "__main__":
    test_vinculo()
