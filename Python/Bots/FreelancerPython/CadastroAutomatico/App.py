from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

# 1 Navegar até o site
# Selenium utiliza 4 navegadores (Chrome, Edge, Firefox e Safari) - Selecionando o navegador
driver = webdriver.Edge() 
# Pegando o link que deseja abrir (Site da UNIVERSIDADE CATOLICA DE SANTOS - LOGIN)
driver.get('https://adfs.unisantos.br/adfs/ls/?SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&SAMLRequest=jZNRb9owEMe%2FiuX3kJAmrWQBEoOuRWIQAd3DXirjXFZLjp35LoV9%2BzmhbFRaUZ9i3f3%2F5%2FudLyOUtWnEtKUXu4FfLSCxY20sij4x5q23wknUKKysAQUpsZ1%2BW4p0kIjGO3LKGX5hue6QiOBJO8vZYj7m69X9cv2wWD3f5vmtUiqP0mECUVbdlZHcZ1WUZHfZDUAucyU5%2Bw4eg3fMQ6lQALGFhUWSlkIoSbMgj4b5LrkRaS6S%2FAdnhXevugS%2FCp2M%2BZPVGMQOOZsHUG0l9eVeiBoUcSzLCgftWTTY%2Bz4SG4z7Sj3rF21LbX9ex9yfRCged7siKtbbHWfTM%2FrMWWxr8Fvwr1rB02b5r4PDIX3fQOM8SRN3k42lQj4ZdUfRs%2FvJp2zkW6RRfOkbnV69m8piXjij1W%2F21fla0sdcw8Gwj%2BgyqnqpaC02oHSloQx4xrjDzIOkMOhwJXAWn%2B95Wywo%2BzUL%2FARHYjNXN9Jr7F4AjlLRGe5SNTNhZTZQTa5ulRKq04VwET4H58s33v%2BWOuU%2BaOtv9vKXmPwB&RelayState=http%3A%2F%2Fww2.unisantos.br%2Fportal%2Flogin&Signature=tcOZUohjDLonOABd36XbaKHzrGkbfatBlWE5cCufIlkLgO7IYIYHyB4tQGFd1v62%2BUfoA0yBLViy8%2BmSa7QvQLDtxqqm02Tpg2VbDjJEy5aAjqb8Jl67eJH7SK3YxOM6k7Fk7Q1OgBbJIrA3r4rkABpwCVqKnNH12JGLcWmOttCit8tgviSdi6B4aOxyUYk3y%2Bbo6IGodzZ3UnjgUgc30n6ZjfFVj2BC2Dv4M1dJ1aVTwLrI3BXebJel17zcE1IMSNrUBbuuVBCIW58%2F2tjau07XZ1v%2FLWmzSgm182lWS3IVmj7ltzTMLTdj6Gs4OxJ1ziVkkIMMBJV7dRfJ5lKN%2Fw%3D%3D') 
# dalay para abrir a pagina, sleep pode conter valores flutuantes
sleep(1) 

# 2 Digitar o email e senha
email = driver.find_element(By.XPATH, "//input[@id='rawUserNameInput']").send_keys('email') # Guardei ambos em variaveis para possiveis usos futuros
senha = driver.find_element(By.XPATH, "//input[@id='passwordInput']").send_keys('senha')
sleep(2)

# 3 clicar em entrar
driver.find_element(By.XPATH, "//span[@id='submitButton']").click()
sleep(0.2) # Pausa de 2 segundos

# Já acessamos o site - agora vamos entrar no moodle
driver.find_element(By.XPATH, "//a[@href='acessoMoodle']").click()
sleep(2)

# Encerramento do bot pelo terminal
input('Digite enter no terminal para encerrar!')
driver.quit()

# Acesse o link para aprender mais sobre a biblioteca selenium
#https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwibpqfXy8qFAxUDrJUCHYayAyUQFnoECAcQAQ&url=https%3A%2F%2Fselenium-python.readthedocs.io%2F&usg=AOvVaw3bqFWMRibDw9O_2DRf9j_8&opi=89978449