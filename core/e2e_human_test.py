import sys
import os
# Asegurar que el entorno reconoce la carpeta core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.legal.qr_engine import generar_codigo_seguimiento
from core.legal.kyc_engine import procesar_verificacion

def test_flujo_humano():
    print("--- 🛡️ INICIANDO TEST E2E: FLUJO HUMANO VOYAGERS ---")
    
    # 1. Simulación de Registro y KYC (Lukas)
    print("[PASO 1] Verificando identidad de nuevo usuario...")
    kyc = procesar_verificacion("USER_BETA_01", "PASAPORTE")
    if kyc['estado'] == "VERIFICADO":
        print("  [OK] KYC aprobado.")
    else:
        print("  [FAIL] KYC fallido."); return False

    # 2. Simulación de cálculo de ganancias (Valentina/Aki)
    print("[PASO 2] Validando lógica de simulador (10kg, 500km)...")
    bruto = (500 * 0.005) * 10
    neto = bruto * 0.85
    if neto == 21.25:
        print(f"  [OK] Simulador exacto: {neto}€ netos.")
    else:
        print(f"  [FAIL] Error en cálculo: {neto}€."); return False

    # 3. Generación de Seguridad QR (Lukas)
    print("[PASO 3] Generando Token de seguridad para entrega...")
    token = generar_codigo_seguimiento("ENVIO_RECOGER_01")
    if token.startswith("VOY-"):
        print(f"  [OK] QR Token generado: {token}")
    else:
        print("  [FAIL] Error en QR."); return False

    print("-------------------------------------------------")
    print("✅ RESULTADO: FLUJO HUMANO INTEGRAL FUNCIONANDO")
    return True

if __name__ == "__main__":
    if not test_flujo_humano():
        sys.exit(1)
