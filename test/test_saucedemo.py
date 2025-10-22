import pytest
import sys
from selenium.webdriver.common.by import By
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo, get_driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='session')
def driver():
    # configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver. quit()


#def test_login(driver):
    #login_saucedemo(driver)
    
    #title = driver.find_element(By.CLASS_NAME, 'title').text
    #assert title == "Products"

#def test_catalogo(driver):
    #login_saucedemo(driver)
    
    #products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    #assert len(products) > 0

#def test_carrito(driver):
    #login_saucedemo(driver)
    
    #wait = WebDriverWait(driver, 10)
    #products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item')))
    
    #if len(products) >= 2:
        # Click en primer producto
        #button1 = products[0].find_element(By.TAG_NAME, 'button')
        #button1.click()
        
        # Click en segundo producto
        #button2 = products[1].find_element(By.TAG_NAME, 'button')
        #button2.click()
        
        # Esperar y verificar el badge
        #badge_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge')))
        #badge_text = badge_element.text
        #assert badge_text == 2


def test_login(driver):

    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'



def test_catalogo(driver):
    login_saucedemo ( driver )

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0

def test_carrito(driver):
    login_saucedemo (driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    
    total_products = len(products) 

    if total_products >=2:
        products [0]. find_element(By.TAG_NAME, 'button').click()
        
        products [1]. find_element(By.TAG_NAME, 'button').click()


    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert int (badge) == 2
