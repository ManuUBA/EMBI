import re
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_EMBI():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.rava.com/perfil/riesgo%20pais")
        time.sleep(5)  # Wait page load

        body_text = driver.find_element("tag name", "body").text

        match = re.search(r"RIESGO PAIS\s+Argentina\s+([\d.,]+)", body_text, re.IGNORECASE)
        if match:
            EMBI = match.group(1).replace('.', '').replace(',', '.')
            print(f"EMBI: {EMBI}")

            # Save JSON
            with open("EMBI.json", "w", encoding="utf-8") as f:
                json.dump({"EMBI": EMBI}, f)
        else:
            print("EMBI was not found")
    finally:
        driver.quit()

if __name__ == "__main__":
    get_EMBI()



