

#librari gratuite care ne trebuie sa accesam selenium si sa avem acces la chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam chrome - un tab gol de chrome sau ce alt browser vrem
#salvam in variabila chrome tabul gol de chrome

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#maximaze window
chrome.maximize_window()
chrome.get("https://www.kfea.ro/cafea/")
sleep(20)
chrome.find_element(By.ID, "search").send_keys("jacobs")
#pentru alte butoane de pe pagina inafara de literea sau cifre si caractere speciale folosim libraria keys
chrome.find_element(By.ID, "search").send_keys(Keys.ENTER)
sleep(10)
chrome.quit()

