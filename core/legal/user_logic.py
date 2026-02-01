USER_TYPES = {
    "VIAJERO": "Persona física compartiendo maleta/coche.",
    "LOGISTICA": "Empresa de transporte con espacio muerto en ruta.",
    "AEROLINEA": "Venta de bodega excedente en vuelos comerciales."
}

def clasificar_oferta(tipo_usuario, capacidad_kg):
    if tipo_usuario == "VIAJERO" and capacidad_kg > 23:
        return "ALERTA: Exceso de peso para maleta estándar."
    return f"Oferta {tipo_usuario} aceptada por {capacidad_kg}kg."
