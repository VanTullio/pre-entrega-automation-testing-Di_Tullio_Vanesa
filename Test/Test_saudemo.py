import pytest
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
