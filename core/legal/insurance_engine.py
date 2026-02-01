def generar_poliza_seguro(envio_id, valor_paquete):
    return {'id': f'INS-{envio_id}-2026', 'cobertura': min(valor_paquete * 2, 500)}
