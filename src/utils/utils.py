from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import csv

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

def fill_form(driver,educational_level,department,year,term):
    try:
        fill_select(driver,'id', 'formTurma:inputNivel', educational_level)
        fill_select(driver,'id', 'formTurma:inputDepto', department)
        fill_input(driver,'id', 'formTurma:inputAno', year)
        fill_select(driver,'id', 'formTurma:inputPeriodo', term)
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

def retrieve_courses(driver):
    courses = []
    count = 1
    course = {}
    while True:
        try:
            tr = driver.find_element(By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]")
        except NoSuchElementException:
            courses.append(course)
            break
        if tr.get_attribute('class') == 'agrupador': 
            courses.append(course)
            course = {}
            name = tr.find_element(By.CLASS_NAME, "tituloDisciplina").text
            course_name = name.split(' - ', 1)[1]
            course_code = name.split()[0] 
            course['course_name'] = course_name
            course['course_code'] = course_code
        else:
            course['course_number'] = tr.find_element(By.CLASS_NAME, "turma").text
            course['anoPeriodo'] = tr.find_element(By.CLASS_NAME, "anoPeriodo").text
            course['professor'] = tr.find_element(By.CLASS_NAME, "nome").text
            course['horario'] = driver.find_element(By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[4]").text
            course['vagas_ofertadas'] = driver.find_element(By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[6]").text
            course['vagas_ocupadas'] = driver.find_element(By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[7]").text
            course['local'] = driver.find_element(By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[8]").text
        count += 1
        
    return courses[1:]

def json_write(data, file_name):
    with open(f'{file_name}', 'w') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)

def csv_write(data, file_name):
    with open(f'./data/{file_name}.csv', 'w') as csv_file:
        csv_file.write('class_name,class_code,class_number,anoPeriodo,professor,horario,vagas_ofertadas,vagas_ocupadas,local\n')
        for course in data:
            csv_file.write(f"{course['class_name']},{course['class_code']},{course['class_number']},{course['anoPeriodo']},{course['professor']},{course['horario']},{course['vagas_ofertadas']},{course['vagas_ocupadas']},{course['local']}\n")