def verificar_matching_premium(viajero_ruta, empresa_ruta, oferta_eur):
    if viajero_ruta == empresa_ruta:
        return {
            "notificar": True, 
            "msg": f"🔔 ¡OFERTA EXPRESS! {oferta_eur}€ por tu espacio en {viajero_ruta}.",
            "prioridad": "ALTA"
        }
    return {"notificar": False}
