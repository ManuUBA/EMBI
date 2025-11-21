import re
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_EMBI():

    options = Options()

    # Headless moderno
    options.add_argument("--headless=new")

    # Requeridos en GitHub Actions
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Evitar bloqueos de Rava
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"), options=options)

    try:
        driver.set_page_load_timeout(20)
        driver.get("https://www.rava.com/perfil/riesgo%20pais")

        # Espera manual breve
        time.sleep(4)

        body = driver.find_element("tag name", "body").text

        # Expresión robusta
        match = re.search(
            r"RIESGO\s+PA[IÍ]S\s+Argentina\s+([\d.,]+)", 
            body, 
            re.IGNORECASE
        )

        if match:
            embi_value = match.group(1).replace(".", "").replace(",", ".")
            print("EMBI:", embi_value)

            with open("EMBI.json", "w", encoding="utf-8") as f:
                json.dump({"EMBI": embi_value}, f)
        else:
            print("❌ No se encontró el valor del EMBI en el HTML.")
            print("--- BODY ---")
            print(body[:2000])

    finally:
        driver.quit()


if __name__ == "__main__":
    get_EMBI()
