import uuid

def generar_codigo_seguimiento(envio_id):
    # Generamos un token único que será el contenido del QR
    token_seguridad = f"VOY-{uuid.uuid4().hex[:8].upper()}"
    print(f"[LUKAS] Token QR generado para {envio_id}: {token_seguridad}")
    return token_seguridad

# Simulación de validación de escaneo
def validar_escaneo(token_presentado, token_real):
    return token_presentado == token_real
