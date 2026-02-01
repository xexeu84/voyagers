def generar_poliza_seguro(envio_id, valor_paquete):
    """Genera una póliza simulada con cobertura máxima de 500€."""
    return {'id': f'INS-{envio_id}-2026', 'cobertura': min(valor_paquete * 2, 500)}
