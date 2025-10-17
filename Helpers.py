from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time
URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():

    options = Options()
    Options.add_argument('--start-maximized') # abre la pag maximizada

    Service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(Service = Service)

    time.sleep(5)
    return driver

def loguin_saucedemo( driver ):

    driver.get(URL) # es una variable definida mas arriba abrir la url
    
    
    driver.find_element(By.NAME,'user-name').send_keys(USERNAME) #iniciar sesion
    driver.find_element(By.NAME,'password').send_key(PASSWORD)
    driver.find_element(By.ID,'loguin-button').click()
    
    time.sleep(7)


