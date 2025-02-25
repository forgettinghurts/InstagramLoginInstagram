from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuración para usar webdriver_manager y evitar problemas con el chromedriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abre Instagram
driver.get("https://www.instagram.com")

# Realiza las acciones necesarias aquí (por ejemplo, login, navegación, etc.)
# Recuerda que para interactuar con el sitio, puedes usar métodos de Selenium como `find_element_by_name()`, `find_element_by_id()`, etc.

# Mantén el navegador abierto
input("Presiona Enter para salir...")

# Cierra el navegador al finalizar
driver.quit()
