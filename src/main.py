"""
Main module for retrieving course data from the SIGAA platform.

This script utilizes the Selenium library to automate the process of fetching course information
from the SIGAA platform for specific departments during a particular academic term.
The data is extracted and saved in a structured format (JSON).

Dependencies:
- json
- selenium.webdriver
- utils.utils (custom utility functions)

Usage:
- Configure the desired educational level, academic year, and term in the script.
- Run the script to initiate the automated process of retrieving and saving course information.

Example:
    python3 main.py

"""
import json
from selenium import webdriver
from utils.utils import fill_form, form_submit, button_click, retrieve_courses, json_write


if __name__ == '__main__':
    # Abre arquivo com dados dos departamentos
    with open('./data/department_list.json', 'r') as json_file:
        department_list = json.load(json_file)

    # Definir a URL que você quer acessar
    URL = 'https://sigaa.unb.br/sigaa/public/turmas/listar.jsf'

    # Iniciar o navegador e acesse a página
    driver = webdriver.Chrome()  # ou webdriver.Firefox(), dependendo do seu navegador
    driver.get(URL)

    # Defina os inputs da busca
    EDUCATIONAL_LEVEL = 'G'
    YEAR = '2024'
    TERM = '1'

    decent_department_list = [
        {"name": "DEPARTAMENTO DE MATEMÁTICA", "value": "518"},
        {"name": "DEPARTAMENTO DE CIÊNCIAS DA COMPUTAÇÃO", "value": "508"},
        {"name": "DEPARTAMENTO DE ENGENHARIA ELÉTRICA", "value": "443"},
    ]

    # Insere os departamentos e suas turmas em uma lista
    all_courses_data = []
    for i, department in enumerate(decent_department_list):
        department_classes = {}

        # Preencher os inputs da busca
        fill_form(driver, EDUCATIONAL_LEVEL, department['value'], YEAR, TERM)

        # Submeter o formulário
        form_submit(driver, 'id', 'formTurma')
        button_click(driver, 'name', 'formTurma:j_id_jsp_1370969402_11')

        # Retornar turmas
        courses = retrieve_courses(driver)

        department_classes['departmento'] = department['name']
        department_classes['courses'] = courses
        all_courses_data.append(department_classes)

    # Salva os dados em um arquivo json
    JSON_FILE_PATH = './data/courses_data.json'
    json_write(all_courses_data, JSON_FILE_PATH)

    # Impede que o navegador feche caso seja necessário inspecionar o código
    # while(True):
    #     pass
