def test_calculo_ganancia(peso, distancia):
    bruto = (distancia * 0.005) * peso
    comision = bruto * 0.15
    neto = bruto - comision
    return round(neto, 2)

# Verificación de lógica real: 10kg a 1000km debería dar 42.50€
resultado = test_calculo_ganancia(10, 1000)
print(f"--- TEST MATEMÁTICO VOYAGERS ---")
if resultado == 42.5:
    print(f"[OK] Cálculo exacto: {resultado}€")
else:
    print(f"[FAIL] Error en simulación: {resultado}€")
