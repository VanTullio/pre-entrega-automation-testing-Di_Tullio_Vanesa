import pytest
from selenium.webdriver.common.by import By
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from Utils.Helpers import loguin_saucedemo, get_driver

@pytest.fixture #(scope = 'session') #permite que no cierre el navegador y se mantiene abierto
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):
    loguin_saucedemo (driver)
    assert "/inventory.html" in driver.current_url
    titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'
    print("TEST PASSED : LOGIN SUCCESSFUL") # verifica que inicia sesion y entramos al catalogo

def test_catalogo( driver ):
    loguin_saucedemo( driver )
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    print("TEST PASSED : ") #verifica que existen prod en catalogo


def test_carrito(driver):
    loguin_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    products[0].find_element(By.TAG_NAME, 'button').click()
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == "1"  
    print("TEST PASSED : ADD TO CART") #verifica que se adiciona 1 prod al carrito




"""def Log_out(driver):
    loguin_saucedemo (driver)
    assert "/inventory.html" in driver.current_url
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    time.sleep(3)
    logout_link = driver.find_element(By.ID,"logout_sidebar_link")
    logout_link.click()
    assert "saucedemo.com" in driver.current_url """  #verifica que se cierra sesion (pero no corre!)
    

