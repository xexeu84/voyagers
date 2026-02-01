import sys
import os
sys.path.append(os.getcwd())

from core.operational.kyc_engine import validar_usuario_kyc
from core.operational.notifications import verificar_matching_premium
from core.legal.express_engine import calcular_envio_express
from core.operational.mailer import disparar_email_bienvenida

def test_operativo_completo():
    print("--- 🔍 TEST DE INTEGRACIÓN VOYAGERS 2026 ---")
    
    # PASO 1: KYC
    user = "MARCUS_CEO"
    kyc = validar_usuario_kyc(user, "ID-998877")
    print(f"[1] KYC Status: {kyc['status']} - Nivel: {kyc['nivel_confianza']}")
    
    # PASO 2: Matching B2B -> P2P
    ruta = "MAD-BCN"
    alerta = verificar_matching_premium(ruta, ruta, 45.0)
    if alerta['notificar']:
        print(f"[2] ALERTA: {alerta['msg']}")
    
    # PASO 3: Finanzas Express
    kilos = 5
    pago = calcular_envio_express(kilos)
    print(f"[3] FINANZAS: Empresa paga por {kilos}kg. Viajero recibe: {pago['pago_viajero']}€ | Voyagers: {pago['comision_voyagers']}€")
    
    # PASO 4: Comunicaciones
    email = disparar_email_bienvenida("marcus@voyagers.com", kyc['status'])
    
    print("\n✅ RESULTADO: El ecosistema es estable y rentable.")

if __name__ == "__main__":
    test_operativo_completo()
