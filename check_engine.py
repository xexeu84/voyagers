import sys
import os
# Forzamos la ruta raíz en el sistema
sys.path.append(os.getcwd())

try:
    from core.legal.qr_engine import generar_codigo_seguimiento
    from core.legal.insurance_engine import generar_poliza_seguro
    
    print("\n--- 🛡️ VOYAGERS: MOTOR STATUS ---")
    token = generar_codigo_seguimiento("MARCUS_FINAL_V4")
    seguro = generar_poliza_seguro("MARCUS_FINAL_V4", 100)
    print(f"  [OK] QR: {token}")
    print(f"  [OK] SEGURO: {seguro['id']}")
    print("--- ✅ TODO FUNCIONA CORRECTAMENTE ---")
except Exception as e:
    print(f"\n❌ ERROR DE RUTA: {e}")
    print(f"Directorio actual: {os.getcwd()}")
