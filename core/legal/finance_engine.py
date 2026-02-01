def calcular_comision(monto_pago):
    tarifa_fija = 2.50  # Euros
    porcentaje_voyagers = 0.15  # 15%
    
    comision = tarifa_fija + (monto_pago * porcentaje_voyagers)
    pago_conductor = monto_pago - comision
    
    return {
        "monto_total": monto_pago,
        "comision_voyagers": round(comision, 2),
        "pago_conductor": round(pago_conductor, 2),
        "moneda": "EUR"
    }
