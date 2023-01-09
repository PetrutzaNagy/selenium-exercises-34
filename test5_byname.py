#librari gratuite care ne trebuie sa accesam selenium si sa avem acces la chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam chrome - un tab gol de chrome sau ce alt browser vrem
#salvam in variabila chrome tabul gol de chrome

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#maximaze window
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
sleep(5)
#daca are atributul name adica vedem name = "..." putem folosi By name
username_input = chrome.find_element(By.NAME, "username")
username_input.send_keys("tomsmith")
chrome.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
sleep(10)
#ne inchide fereastra de crome
chrome.quit()
