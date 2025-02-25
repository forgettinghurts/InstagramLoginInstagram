from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Configura el driver (Asegúrate de tener el path correcto a tu ChromeDriver)
driver = webdriver.Chrome(executable_path='/ruta/a/tu/chromedriver')

# Abre la página de inicio de sesión de Instagram
driver.get("https://www.instagram.com/accounts/login/")

# Espera un poco a que la página cargue
sleep(3)

# Encuentra los campos de correo y contraseña
email_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

# Introduce tus datos
email_field.send_keys("forgettinghurts@gmail.com")
password_field.send_keys("22004411991199A.a")

# Envía el formulario
password_field.send_keys(Keys.RETURN)

# Espera un poco para que cargue la página siguiente
sleep(5)

# Aquí puedes agregar más acciones (por ejemplo, verificar si el inicio de sesión fue exitoso)
print("Iniciado sesión con éxito")

# Cierra el navegador
driver.quit()
