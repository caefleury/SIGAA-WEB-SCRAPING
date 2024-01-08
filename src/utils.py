from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Encontra o select e o preenche com os valores
def fill_select(driver,tag,atribute_value,select_value):
    try:
        select_element = driver.find_element(tag, atribute_value)
        select = Select(select_element)
        select.select_by_value(select_value)
    except NoSuchElementException as e:
        return e

def fill_input(driver,tag,atribute_value,input_value):
    try:
        input_element = driver.find_element(tag, atribute_value)
        input_element.clear() 
        input_element.send_keys(input_value)
    except NoSuchElementException as e:
        return e

def form_submit(driver,tag,atribute_value):
    try:
        form_element = driver.find_element(tag, atribute_value)
        form_element.submit()
    except NoSuchElementException as e:
        return e
    
def button_click(driver,tag,atribute_value):
    try:
        button_element = driver.find_element(tag, atribute_value)
        button_element.click()
    except NoSuchElementException as e:
        return e