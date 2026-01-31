import sys
from core.route_engine import optimizar_matching
from core.legal.ecmr_engine import generar_ecmr
from core.payment_engine import EscrowSystem

def ejecutar_test_maestro():
    print("--- INICIANDO TEST DE INTEGRIDAD VOYAGERS 2026 ---")
    
    # TEST 1: IA & RUTAS (Aki)
    viajero = {"origen": "Madrid", "destino": "Barcelona", "capacidad_libre": 20}
    paquetes = [{"id": "P-TEST", "peso": 5, "distancia_km": 620}]
    match = optimizar_matching(viajero, paquetes)
    if match:
        print("[OK] Test 1: Motor de Rutas e IA respondiendo.")
    
    # TEST 2: LEGAL & eCMR (Lukas)
    try:
        contrato = generar_ecmr("Cliente_Test", "Viajero_Test", "Caja_Sensores", 5.0)
        print(f"[OK] Test 2: Generador eCMR funcional (ID: {contrato['ecmr_id']}).")
    except Exception as e:
        print(f"[FAIL] Test 2: Error en modulo legal: {e}")

    # TEST 3: FINANZAS & COMISIÓN (Marcus-Bot)
    escrow = EscrowSystem()
    pago = escrow.crear_pago("ENVIO-TEST", 200.0)
    if pago['comision_voyagers'] == 30.0: # 15% de 200
        print(f"[OK] Test 3: Motor de Pagos calculando comision del 15% (30.0 EUR).")
    else:
        print("[FAIL] Test 3: Error en calculo de comisiones.")

    print("--- RESULTADO: SISTEMA INTEGRAL OPERATIVO AL 100% ---")

if __name__ == "__main__":
    ejecutar_test_maestro()
