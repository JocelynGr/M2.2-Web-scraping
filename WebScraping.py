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

    # Paso 1: Abre Wikipedia

    driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")


    # Espera a que el cuadro de búsqueda esté presente

    search_box = WebDriverWait(driver, 10).until(

        EC.presence_of_element_located((By.ID, "searchInput"))

    )

    search_box.send_keys("TecNM")

    search_box.submit()


    # Espera a que aparezcan los resultados

    pachuca_link = WebDriverWait(driver, 10).until(

        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Instituto Tecnológico de Pachuca"))

    )

    pachuca_link.click()


    # Espera a que la página del Instituto Tecnológico de Pachuca se cargue

    oferta_academica_link = WebDriverWait(driver, 10).until(

        EC.presence_of_element_located((By.LINK_TEXT, "Oferta académica"))

    )

    oferta_academica_link.click()


finally:

    # Mantén el navegador abierto

    input("Presiona Enter para cerrar el navegador...")

    driver.quit()