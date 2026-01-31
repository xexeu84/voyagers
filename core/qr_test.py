from core.legal.qr_engine import generar_codigo_seguimiento, validar_escaneo

print("--- 🛡️ TEST DE SEGURIDAD QR ---")
token = generar_codigo_seguimiento("ENVIO_001")
if token.startswith("VOY-") and len(token) == 12:
    print(f"  [OK] Generación de Token: {token}")
    if validar_escaneo(token, token):
        print("  [OK] Validación de Escaneo: Exitosa.")
    else:
        print("  [FAIL] Validación: Error de concordancia.")
else:
    print("  [FAIL] Estructura de Token inválida.")
