import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'core'))

try:
    from legal.insurance_engine import generar_poliza_seguro
    res = generar_poliza_seguro("TEST", 100)
    print(f"\n✅ MOTOR LOCALIZADO: Poliza {res['id']} activa.")
except Exception as e:
    print(f"\n❌ ERROR TODAVIA: {e}")
