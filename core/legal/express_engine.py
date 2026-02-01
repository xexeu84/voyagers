def calcular_envio_express(kilos, es_empresa=True):
    # Tarifa premium por rapidez (el viajero gana más, nosotros también)
    tarifa_express_por_kilo = 12.0  
    subtotal = kilos * tarifa_express_por_kilo
    
    # Comisión Voyagers (Premium 25% por gestión B2B/P2P)
    comision_v = subtotal * 0.25
    pago_viajero = subtotal - comision_v
    
    return {
        "tipo": "EXPRESS_B2B",
        "pago_viajero": round(pago_viajero, 2),
        "comision_voyagers": round(comision_v, 2),
        "entrega_estimada": "Mismo día (Ruta del Viajero)"
    }
