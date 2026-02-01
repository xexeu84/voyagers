﻿import uuid

class EscrowSystem:
    def __init__(self, comision_rate=0.15, fixed_fee=2.50):
        self.comision_rate = comision_rate
        self.fixed_fee = fixed_fee
        self.transacciones = {}

    def crear_pago(self, envio_id, monto_total):
        transaccion_id = f"PAY-{str(uuid.uuid4())[:6].upper()}"
        comision = (monto_total * self.comision_rate) + self.fixed_fee
        pago_viajero = monto_total - comision
        
        self.transacciones[envio_id] = {
            "id": transaccion_id,
            "monto_total": monto_total,
            "comision_voyagers": comision,
            "pago_viajero": pago_viajero,
            "estado": "RETENIDO_ESCROW"
        }
        return self.transacciones[envio_id]

    def liberar_pago(self, envio_id):
        if envio_id in self.transacciones:
            self.transacciones[envio_id]["estado"] = "LIQUIDADO"
            return True
        return False

# Prueba de concepto del primer cobro de comision
escrow = EscrowSystem()
pago = escrow.crear_pago("ENVIO-001", 100.0)
print(f"[FINANZAS] Pago retenido. Comision Voyagers: {pago['comision_voyagers']} EUR")
