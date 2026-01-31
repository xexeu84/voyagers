import telebot
import time

# Lukas: Nuevo Token verificado de tu captura de las 19:22
TOKEN = "8300141763:AAHEAQp8iGFumFoaAjyGESiMAPSR0wUVAEc"

bot = telebot.TeleBot(TOKEN)

def activar_sistema():
    try:
        me = bot.get_me()
        print(f"✅ AKI: Conexión establecida con @{me.username}")
        print("[*] Escribe 'HOLA' en el chat del bot en tu Telegram ahora...")
        
        # Esperamos a que nos escribas para capturar tu ID real
        timeout = 30
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            updates = bot.get_updates()
            if updates:
                chat_id = updates[-1].message.chat.id
                print(f"✅ LUKAS: ID de Mando detectado: {chat_id}")
                bot.send_message(chat_id, "🚀 **SISTEMA VOYAGERS 2026 ONLINE**\nComunicaciones blindadas. Esperando órdenes de Marcus.")
                return chat_id
            time.sleep(2)
            
        print("❌ TIMEOUT: No recibí mensajes. ¿Le diste a 'INICIAR'?")
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    activar_sistema()