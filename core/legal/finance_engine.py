def calcular_p2p(kilos, valor_declarado):
    precio_por_kilo = 5.0  # Media de ahorro vs mensajería oficial
    pago_al_viajero = kilos * precio_por_kilo
    comision_voyagers = pago_al_viajero * 0.20  # 20% por conectar usuarios
    
    return {
        "kilos": kilos,
        "pago_viajero": pago_al_viajero,
        "comision": round(comision_voyagers, 2),
        "ahorro_estimado_cliente": "50% vs DHL/UPS"
    }
