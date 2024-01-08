from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

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
    
def print_page_source(driver):
    print(driver.page_source)

def retrieve_classes(driver):
    classes = []
    count = 1
    turma = {}
    while True:
        try:
            tr = driver.find_element(By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]")
        except NoSuchElementException:
            break
        if tr.get_attribute('class') == 'agrupador': 
                    classes.append(turma)
                    turma = {}
                    name = tr.find_element(By.CLASS_NAME, "tituloDisciplina").text
                    class_name = name.split(' - ', 1)[1]
                    class_code = name.split()[0]
                    turma['class_name'] = class_name
                    turma['class_code'] = class_code
        else:
            turma['class_number'] = tr.find_element(By.CLASS_NAME, "turma").text
            turma['anoPeriodo'] = tr.find_element(By.CLASS_NAME, "anoPeriodo").text
            turma['professor'] = tr.find_element(By.CLASS_NAME, "nome").text
            turma['horario'] = driver.find_element(By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[4]").text
            turma['vagas_ofertadas'] = driver.find_element(By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[6]").text
            turma['vagas_ocupadas'] = driver.find_element(By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[7]").text
            turma['local'] = driver.find_element(By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[8]").text

        count += 1
        
    return classes