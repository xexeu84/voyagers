import sys
import os
# Añadir el directorio actual al path para evitar ModuleNotFoundError
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from core.legal.qr_engine import generar_codigo_seguimiento, validar_escaneo

print("--- 🛡️ TEST DE SEGURIDAD QR (CORREGIDO) ---")
token = generar_codigo_seguimiento("ENVIO_REAL_01")
if token.startswith("VOY-"):
    print(f"  [OK] Token generado: {token}")
    print("  [OK] Test de integridad de módulos: PASADO")
else:
    print("  [FAIL] Error en la lógica de tokens.")
    sys.exit(1)
