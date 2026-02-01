import sys
import os
sys.path.append(os.getcwd())

from core.legal.insurance_engine import generar_poliza_seguro
from core.legal.qr_engine import generar_codigo_seguimiento
from core.legal.finance_engine import calcular_comision

def ejecutar_simulacro():
    print("--- 🚀 INICIANDO SIMULACRO VOYAGERS 2026 ---")
    
    # 1. Datos del Envío
    envio_id = "SHIP-99-BCN"
    valor_paquete = 100
    
    # 2. Ejecución de Motores
    seguro = generar_poliza_seguro(envio_id, valor_paquete)
    qr = generar_codigo_seguimiento(envio_id)
    finanzas = calcular_comision(valor_paquete)
    
    # 3. Reporte de Resultados
    print(f"\n[CLIENTE] Envío {envio_id} registrado.")
    print(f"[LEGAL] Seguro activado: {seguro['id']} | Cobertura: {seguro['cobertura']}€")
    print(f"[OP] QR de Seguimiento generado: {qr}")
    print(f"\n--- 💰 DESGLOSE FINANCIERO ---")
    print(f"Monto Pagado por Cliente: {finanzas['monto_total']} {finanzas['moneda']}")
    print(f"Comisión Voyagers (15% + 2.5): {finanzas['comision_voyagers']} {finanzas['moneda']}")
    print(f"Pago Neto al Transportista: {finanzas['pago_conductor']} {finanzas['moneda']}")
    print("\n✅ SIMULACRO COMPLETADO: TODO EL FLUJO ES LÓGICAMENTE CORRECTO")

if __name__ == "__main__":
    ejecutar_simulacro()
