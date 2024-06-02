from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# ...
driver.get("https://www.cartoesmaisbarato.com.br/")
time.sleep(10)