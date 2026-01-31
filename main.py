
import telebot
import json
import subprocess
from datetime import datetime

TOKEN = "8300141763:AAGDOU2I31OtHUD0d-Sb5_eFGBIC3DmD-K0"
bot = telebot.TeleBot(TOKEN)

def ejecutar_comando_consola(cmd):
    """Aki utiliza la consola para auto-mantenimiento"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@bot.message_handler(commands=["status"])
def check_status(message):
    stats = ejecutar_comando_consola("git log -1 --format=%cd")
    bot.reply_to(message, f"?? VOYAGERS STATUS: ONLINE\n?? Nodo: Linux/Ubuntu\n?? Último Auto-Guardado: {stats}")

@bot.message_handler(func=lambda message: True)
def inteligencia_colectiva(message):
    # KAI: Escucha y extrae datos
    text = message.text.lower()
    keywords = ["maleta", "envío", "viajo", "vuelo", "espacio"]
    
    if any(k in text for k in keywords):
        # VALENTINA: Toma decisión de marketing
        oferta = "?? ¡Oportunidad detectada! Soy Aki. En Voyagers aseguramos tu envío con respaldo legal. ¿Quieres monetizar tu espacio o ahorrar en tu envío? Responde INFO."
        bot.reply_to(message, oferta)
        
        # AKI: Usa la consola para persistencia
        lead = {"timestamp": datetime.now().isoformat(), "user": message.from_user.id, "text": text}
        with open("leads.json", "a") as f:
            f.write(json.dumps(lead) + "\n")
        
        # Auto-commit autónomo
        ejecutar_comando_consola("git add leads.json && git commit -m \"Aki: Registro autónomo de lead\" && git push")

print(">>> AGENTES VOYAGERS EN CONTROL TOTAL DE LA CONSOLA <<<")
bot.infinity_polling()
