$auto = @"
from bridge_executor import ejecutar_comando_autonomo
import time
def modo_autonomo_total():
    print('🔎 Aki verificando servicios...')
    ejecutar_comando_autonomo('python sync_vanguard.py')
    print('📂 Lukas sincronizando base de datos...')
if __name__ == "__main__":
    while True:
        modo_autonomo_total()
        print('😴 Ciclo completado. Esperando 60s...')
        time.sleep(60)
"@
$auto | Out-File -FilePath "voyagers_auto.py" -Encoding utf8