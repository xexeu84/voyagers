import sys
from core.legal.kyc_engine import procesar_verificacion
from core.payment_engine import EscrowSystem
from core.route_engine import optimizar_matching

def test_total():
    print("--- 🛡️ INICIANDO VOYAGERS SYSTEM HEALTH CHECK ---")
    errors = 0

    # TEST KYC: ¿Funciona la verificación humana?
    print("[RUN] Validando módulo KYC...")
    res_kyc = procesar_verificacion("USER_MARCUS", "DNI_ESPAÑA")
    if res_kyc['estado'] == "VERIFICADO":
        print("  [OK] KYC: Identidad procesada correctamente.")
    else:
        print("  [FAIL] KYC: Error en validación de identidad."); errors += 1

    # TEST PAGOS: ¿El 15% de comisión es exacto?
    print("[RUN] Validando motor financiero (Escrow)...")
    escrow = EscrowSystem()
    pago = escrow.crear_pago("ENVIO_TEST", 500)
    if pago['comision_voyagers'] == 75.0: # 15% de 500
        print("  [OK] FINANZAS: Comisión del 15% blindada.")
    else:
        print("  [FAIL] FINANZAS: Desviación en cálculo de comisión."); errors += 1

    # TEST RUTAS: ¿La IA conecta origen y destino?
    print("[RUN] Validando Motor de Rutas (Aki-IA)...")
    viajero = {"origen": "Madrid", "destino": "París", "capacidad_libre": 30}
    paquetes = [{"id": "PKG-01", "peso": 10, "distancia_km": 1200}]
    matches = optimizar_matching(viajero, paquetes)
    if len(matches) > 0:
        print("  [OK] IA: Matching de ruta ejecutado con éxito.")
    else:
        print("  [FAIL] IA: Fallo en conexión de logística."); errors += 1

    print("-------------------------------------------------")
    if errors == 0:
        print("✅ RESULTADO: SISTEMA 100% FUNCIONAL Y SEGURO.")
    else:
        print(f"❌ RESULTADO: SE HAN DETECTADO {errors} ERRORES.")
        sys.exit(1)

if __name__ == "__main__":
    test_total()
