import os.path
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Permisos para leer correos
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def main():
    service = get_service()
    print("\n--- SISTEMA VOYAGERS 2.0 (MODO ESCUCHA ACTIVA) ---")
    print(f">>> [STATUS] Conectado a: voyagers.ceo.marcus@gmail.com")
    
    while True:
        try:
            # Escaneo de mensajes no leídos
            results = service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread').execute()
            messages = results.get('messages', [])
            
            if messages:
                print(f">>> [VALENTINA] ¡Alerta! Detectadas {len(messages)} nuevas órdenes. Revisando contenido...")
                # Aquí Aki procesaría el contenido en el futuro
            else:
                print(">>> [LUKAS] Auditoría: Todo en orden. Escaneando de nuevo en 30s...")
            
            time.sleep(30) 
        except Exception as e:
            print(f">>> [ERR] Error en el bucle: {e}")
            time.sleep(10)

if __name__ == '__main__':
    main()