import datetime
import uuid

def generar_ecmr(remitente, transportista, contenido, peso):
    ecmr_id = str(uuid.uuid4())[:8].upper()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    documento = {
        "ecmr_id": f"VOY-{ecmr_id}",
        "fecha_emision": timestamp,
        "partes": {
            "remitente": remitente,
            "transportista": transportista
        },
        "carga": {
            "descripcion": contenido,
            "peso_kg": peso
        },
        "estado": "FIRMADO_DIGITALMENTE",
        "normativa": "eFTI-2026-COMPLIANT"
    }
    
    # Guardar contrato en la "base de datos" (JSON por ahora para rapidez)
    filename = f"core/legal/ecmr_{ecmr_id}.json"
    import json
    with open(filename, 'w') as f:
        json.dump(documento, f, indent=4)
    
    return documento

if __name__ == "__main__":
    # Prueba de concepto del primer contrato Voyagers
    contrato = generar_ecmr("Cliente_Beta_01", "Marcus_CEO", "Equipaje_Tecnico", 5.5)
    print(f"[LEGAL] eCMR Generado con exito: {contrato['ecmr_id']}")
