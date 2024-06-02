from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
#browser = webdriver.Chrome() caso fosse definir browser

service = Service(executable_path='./chromedriver.exe')
#browser.maximize_window() mesmo parâmetro que o abaixo mas para VSCode, maximiza tela do navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)
# get() acessa o parametro inserido
driver.get("https://www.cartoesmaisbarato.com.br/")
time.sleep(4)
#driver.find_element(By.XPATH, "/html/body/div[2]/header/section[2]/div[4]/div/div[3]/div[1]/span[2]/a[1]").click()
driver.find_element(By.XPATH, "//a[@class='js-trigger-login']").click()
time.sleep(2)