def validar_usuario_kyc(user_id, doc_id, facial_match=True):
    # En producción esto conectaría con una API de validación de documentos
    if len(doc_id) > 5 and facial_match:
        return {
            "user_id": user_id,
            "status": "VERIFICADO",
            "nivel_confianza": "PLATINO",
            "limite_carga_eur": 5000
        }
    return {"status": "PENDIENTE", "error": "Documento inválido o biometría fallida"}
