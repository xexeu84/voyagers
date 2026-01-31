import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Aki: Ahora la función acepta un mensaje personalizado
def enviar_reporte_whatsapp(mensaje_personalizado="Test"):
    numero = "34604952480"
    
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=C:\Users\ADMIN\Voyagers-Cloud\user_data")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Usamos el mensaje que nos llega del Radar
        url = f"https://web.whatsapp.com/send?phone={numero}&text={mensaje_personalizado}"
        driver.get(url)
        
        wait = WebDriverWait(driver, 30)
        chat_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
        time.sleep(2) 
        chat_box.send_keys(Keys.ENTER)
        
        print(f"[!] SINC: Reporte enviado con éxito.")
        time.sleep(5) 
        
    except Exception as e:
        print(f"[?] Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # Si lo ejecutas solo, envía un test
    enviar_reporte_whatsapp("Test de sistema")