from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuración de opciones para el navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Abre el navegador en pantalla completa

# Configuración del controlador
service = Service(ChromeDriverManager().install())

# Inicializa el navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Paso 1: Abre la página de citas
    driver.get("http://quotes.toscrape.com")

    # Espera a que las citas estén presentes en la página
    quotes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
    )

    # Extrae y muestra las citas y los autores
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        print(f"Cita: {text}\nAutor: {author}\n")

finally:
    # Mantén el navegador abierto
    input("Presiona Enter para cerrar el navegador...")
    driver.quit()

