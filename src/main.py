from selenium import webdriver
from utils import *
import json

if __name__ == '__main__':
    # Abre arquivo com dados dos departamentos
    with open('./data/dept_data.json', 'r') as json_file:
        dept_data = json.load(json_file)

    # Defina a URL que você quer acessar
    URL ='https://sigaa.unb.br/sigaa/public/turmas/listar.jsf'

    # Inicie o navegador e acesse a página 
    driver = webdriver.Chrome() # ou webdriver.Firefox(), dependendo do seu navegador
    driver.get(URL)

    # Defia os inputs da busca
    EDUCATIONAL_LEVEL = 'G'
    DEPARTMENT = dept_data[17]['value'] # 30 = Computação  , 17 = Matemática
    YEAR = '2023'
    TERM = '4'

    # Preencha os inputs da busca
    fill_select(driver,'id', 'formTurma:inputNivel', EDUCATIONAL_LEVEL)
    fill_select(driver,'id', 'formTurma:inputDepto', DEPARTMENT)
    fill_input(driver,'id', 'formTurma:inputAno', YEAR)
    fill_select(driver,'id', 'formTurma:inputPeriodo', TERM)

    # Submeta o formulário
    form_submit(driver,'id', 'formTurma')
    button_click(driver,'name', 'formTurma:j_id_jsp_1370969402_11')

    # Retorna as turmas da página
    retrieve_courses(driver)

    # Impede que o navegador feche caso seja necessário inspecionar o código
    while(True):
        pass
