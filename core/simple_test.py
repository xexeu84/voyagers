from core.bridge import *
from core.legal.qr_engine import generar_codigo_seguimiento
from core.legal.insurance_engine import generar_poliza_seguro

print("--- 🛡️ VOYAGERS: VALIDACIÓN DE MOTOR ---")
try:
    token = generar_codigo_seguimiento("MARCUS_CLEAN_V3")
    seguro = generar_poliza_seguro("MARCUS_CLEAN_V3", 100)
    print(f"  [OK] QR: {token}")
    print(f"  [OK] SEGURO: {seguro['id']} ({seguro['cobertura']} EUR)")
    print("--- ✅ SISTEMA OPERATIVO ---")
except Exception as e:
    print(f"  [FAIL] Error: {e}")
