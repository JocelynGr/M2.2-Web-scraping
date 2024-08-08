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
    # Paso 1: Abre Amazon
    driver.get("https://www.amazon.com")

    # Espera a que el cuadro de búsqueda esté presente
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )

    # Introduce el término "laptop" en el cuadro de búsqueda y envía la búsqueda
    search_box.send_keys("laptop")
    search_box.submit()

    # Espera a que aparezcan los resultados
    first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot .s-result-item"))
    )

    # Haz clic en el primer resultado de la lista
    first_result.find_element(By.TAG_NAME, "h2").click()

    # Espera a que la página del producto se cargue por completo
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "add-to-cart-button"))
    )

    # Añade el producto al carrito
    add_to_cart_button.click()

finally:
    # Mantén el navegador abierto
    input("Presiona Enter para cerrar el navegador...")
    driver.quit()
