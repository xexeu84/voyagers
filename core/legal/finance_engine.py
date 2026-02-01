def calcular_comision(valor_paquete):
    """Calcula el desglose financiero con la tarifa fija de gestión."""
    comision_rate = 0.15
    fixed_fee = 2.50
    moneda = "EUR"
    
    comision = (valor_paquete * comision_rate) + fixed_fee
    pago_conductor = valor_paquete - comision
    
    return {
        "monto_total": valor_paquete,
        "comision_voyagers": round(comision, 2),
        "pago_conductor": round(pago_conductor, 2),
        "moneda": moneda
    }