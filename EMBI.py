import re
import time
import json
import undetected_chromedriver as uc

def get_EMBI():
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = uc.Chrome(options=options)

    try:
        driver.get("https://www.rava.com/perfil/riesgo%20pais")
        time.sleep(6)

        body = driver.find_element("tag name", "body").text

        match = re.search(r"RIESGO\s+PA[IÍ]S\s+Argentina\s+([\d.,]+)", body, re.IGNORECASE)

        if match:
            value = match.group(1).replace(".", "").replace(",", ".")
            print("EMBI:", value)

            with open("EMBI.json", "w", encoding="utf-8") as f:
                json.dump({"EMBI": value}, f)
        else:
            print("❌ No se encontró el EMBI.")
            print(body[:2000])

    finally:
        driver.quit()

if __name__ == "__main__":
    get_EMBI()
