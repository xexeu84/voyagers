import uuid

def generar_codigo_seguimiento(envio_id):
    """Genera un token único de seguimiento para el envío."""
    suffix = str(uuid.uuid4())[:8].upper()
    return f"VOY-{envio_id}-{suffix}"