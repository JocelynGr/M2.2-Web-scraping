from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Configuración de opciones para el navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Abre el navegador en pantalla completa

# Configuración del controlador
service = Service(ChromeDriverManager().install())

# Inicializa el navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Paso 1: Abre la página principal del Instituto Tecnológico de Pachuca
    driver.get("https://itp.itpachuca.edu.mx/")

    # Paso 2: Espera a que el menú principal esté presente
    ingenierias_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Ingenierías"))
    )

    # Paso 3: Despliega el menú de Ingenierías y selecciona la opción "Sistemas Computacionales"
    action = ActionChains(driver)
    action.move_to_element(ingenierias_menu).perform()  # Coloca el cursor sobre el menú de "Ingenierías"

    sistemas_computacionales_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sistemas Computacionales"))
    )

    action.move_to_element(sistemas_computacionales_option).click().perform()  # Selecciona "Sistemas Computacionales"

    # Paso 4: Deslízate hasta el texto que dice "Retícula 2021"
    reticula_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Retícula 2021"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", reticula_link)  # Desplaza la página hasta el enlace

    # Paso 5: Doble clic en el enlace de "Retícula 2021" y abre en una nueva pestaña
    action.double_click(reticula_link).perform()

    # Cambia a la nueva pestaña
    driver.switch_to.window(driver.window_handles[-1])

finally:
    # Mantén el navegador abierto
    input("Presiona Enter para cerrar el navegador...")
    driver.quit()
