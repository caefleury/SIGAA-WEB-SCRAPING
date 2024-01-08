from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import json
from utils import fill_select, fill_input, form_submit, button_click, retrieve_classes

# Abrir arquivo com dados dos departamentos
with open('./data/depto_data.json', 'r') as json_file:
    depto_data = json.load(json_file)

# Defina a URL que você quer acessar
URL ='https://sigaa.unb.br/sigaa/public/turmas/listar.jsf'

# Inicie o navegador e acesse a página 
driver = webdriver.Chrome() # ou webdriver.Firefox(), dependendo do seu navegador
driver.get(URL)

# Defia os inputs da busca
nivel = 'G'
depto = depto_data[17]['value'] # 30 = Computação  , 17 = Matemática
ANO = '2023'
PERIODO = '4'

# Preencha os inputs da busca
fill_select(driver,'id', 'formTurma:inputNivel', nivel)
fill_select(driver,'id', 'formTurma:inputDepto', depto)
fill_input(driver,'id', 'formTurma:inputAno', ANO)
fill_select(driver,'id', 'formTurma:inputPeriodo', PERIODO)

# Submeta o formulário
form_submit(driver,'id', 'formTurma')
button_click(driver,'name', 'formTurma:j_id_jsp_1370969402_11')

# Retornar a informação das turmas
retrieve_classes(driver)

      
# Impede que o navegador feche para fins de teste
while(True):
    pass
