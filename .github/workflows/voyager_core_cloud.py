import os
import json
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def run_cloud_autonomy():
    print(">>> [LUKAS] Iniciando ciclo en la nube...")
    
    # Recuperar credenciales desde los secretos de la nube
    token_data = os.environ.get('GMAIL_TOKEN')
    if not token_data:
        print(">>> [ERR] No hay token en la nube.")
        return

    creds = Credentials.from_authorized_user_info(json.loads(token_data))
    service = build('gmail', 'v1', credentials=creds)

    # Lógica de Aki: Buscar órdenes
    results = service.users().messages().list(userId='me', q='is:unread').execute()
    messages = results.get('messages', [])

    if messages:
        print(f">>> [VALENTINA] {len(messages)} órdenes encontradas. Procesando...")
        # Aquí ejecutamos la lógica de despliegue
    else:
        print(">>> [AKI] Sin novedades. Entrando en modo ahorro.")

if __name__ == "__main__":
    run_cloud_autonomy()