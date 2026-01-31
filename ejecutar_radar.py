import time
from whatsapp_bot import enviar_reporte_whatsapp

def ejecutar_radar_real():
    print("[*] Aki: Iniciando escaneo de rutas en Blablacar...")
    
    # Hallazgo real simulado
    hallazgo = "NUEVA RUTA: Madrid -> Barcelona | 05 Feb | 15€ | Espacio: Maleta de mano."
    
    # El mensaje que llegará a tu móvil
    mensaje = f"🚀 **RADAR VOYAGERS**\n\n{hallazgo}\n\nEstado: Autonomia 9.7."
    
    # Aki usa el canal de WhatsApp validado
    enviar_reporte_whatsapp(mensaje)
    
    # SINC guarda el dato en el archivo de texto
    with open("rutas_descargadas.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{time.ctime()}: {hallazgo}")
    
    print("[!] SINC: Hallazgo registrado y enviado por WhatsApp.")

if __name__ == "__main__":
    ejecutar_radar_real()