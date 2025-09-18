import re
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def extraer_riesgo_pais_rava():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.rava.com/perfil/riesgo%20pais")
        time.sleep(5)  # Esperar que cargue la página

        body_text = driver.find_element("tag name", "body").text

        match = re.search(r"RIESGO PAIS\s+Argentina\s+([\d.,]+)", body_text, re.IGNORECASE)
        if match:
            riesgo = match.group(1).replace('.', '').replace(',', '.')
            print(f"🟢 Riesgo País: {riesgo}")

            # Guardar en JSON para GitHub Actions o WordPress
            with open("riesgo_pais.json", "w", encoding="utf-8") as f:
                json.dump({"valor": riesgo}, f)
        else:
            print("🔴 No se pudo encontrar el valor del Riesgo País.")
    finally:
        driver.quit()

if __name__ == "__main__":
    extraer_riesgo_pais_rava()
