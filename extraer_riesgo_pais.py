import re
import time
import json
from selenium import webdriver

def extraer_riesgo_pais_rava():
    # Configuración de Chromium
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar sin abrir ventana
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Usamos executable_path porque Selenium 3 no soporta service=
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)

    try:
        driver.get("https://www.rava.com/perfil/riesgo%20pais")
        time.sleep(5)  # Esperar que cargue la página

        body_text = driver.find_element_by_tag_name('body').text

        match = re.search(r"RIESGO PAIS\s+Argentina\s+([\d.,]+)", body_text, re.IGNORECASE)
        if match:
            riesgo = match.group(1).replace('.', '').replace(',', '.')
            print(f"🟢 Riesgo País: {riesgo}")

            # Guardar en JSON para WordPress
            with open("riesgo_pais.json", "w", encoding="utf-8") as f:
                json.dump({"valor": riesgo}, f)
        else:
            print("🔴 No se pudo encontrar el valor del Riesgo País.")
    finally:
        driver.quit()

if __name__ == "__main__":
    extraer_riesgo_pais_rava()
