from selenium import webdriver
from utils.utils import *
import json

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
    for i in range(len(decent_department_list)):
        department_classes = {}
        department = decent_department_list[i]['value']

        # Preencher os inputs da busca
        fill_form(driver, EDUCATIONAL_LEVEL, department, YEAR, TERM)

        # Submeter o formulário
        form_submit(driver, 'id', 'formTurma')
        button_click(driver, 'name', 'formTurma:j_id_jsp_1370969402_11')

        # Retornar turmas
        courses = retrieve_courses(driver)

        department_classes['departmento'] = decent_department_list[i]['name']
        department_classes['courses'] = courses
        all_courses_data.append(department_classes)

    # Salva os dados em um arquivo json
    json_file_path = './data/courses_data.json'
    json_write(all_courses_data, json_file_path)

    # Impede que o navegador feche caso seja necessário inspecionar o código
    # while(True):
    #     pass
