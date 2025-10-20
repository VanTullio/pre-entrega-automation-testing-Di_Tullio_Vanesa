import pytest
from selenium.webdriver.common.by import By
import sys
import os
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

def test_catalogo( driver ):
    loguin_saucedemo( driver )

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0

def test_carrito( driver ):
    loguin_saucedemo( driver )

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
   
    assert len(products) > 0

    products[0].find_element(By.TAG_NAME, 'button').click()

    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == "1"  

