def obtener_ranking_viajero(user_id):
    # Simulación de consulta a DB de GitHub
    reputacion = {
        "MARCUS_CEO": {"estrellas": 5.0, "envios": 124, "status": "VERIFICADO"},
        "GUEST_USER": {"estrellas": 0.0, "envios": 0, "status": "NUEVO"}
    }
    return reputacion.get(user_id, {"estrellas": 3.0, "envios": 1, "status": "ESTÁNDAR"})
