from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import json
from utils import return_depto_by_name

# Dados do departamento
with open('./data/depto_data.json', 'r') as json_file:
    depto_data = json.load(json_file)


# Defina a URL que você quer acessar
URL ='https://sigaa.unb.br/sigaa/public/turmas/listar.jsf'

# Inicie o navegador
driver = webdriver.Chrome() # ou webdriver.Firefox(), dependendo do seu navegador

# Acesse a página
driver.get(URL)
print(json)

try:
    select_element_nivel = driver.find_element('id', 'formTurma:inputNivel')
    select_element_depto = driver.find_element('id', 'formTurma:inputDepto')
    input_element_ano = driver.find_element('id', 'formTurma:inputAno')
    select_element_periodo = driver.find_element('id', 'formTurma:inputPeriodo')
except NoSuchElementException as e:
    if 'formTurma:inputNivel' in str(e):
        print("Nivel element not found")
    elif 'formTurma:inputDepto' in str(e):
        print("Depto element not found")
    elif 'formTurma:inputAno' in str(e):
        print("Ano element not found")
    elif 'formTurma:inputPeriodo' in str(e):
        print("Periodo element not found")

# Selecione o nivel com value='G'
select_nivel = Select(select_element_nivel)
select_nivel.select_by_value('G')

# Selecione o departamento 
depto = depto_data[30]['value'] # 30 = Computação
select_depto = Select(select_element_depto)
select_depto.select_by_value(depto)

# Seleciona o ano
ANO = '2024'
input_element_ano.clear() 
input_element_ano.send_keys(ANO)

# Selecione o periodo
PERIODO = '1'
select_periodo = Select(select_element_periodo)
select_periodo.select_by_value(PERIODO)

# Submeta o formulário
form_element = driver.find_element('name', 'formTurma')
form_element.submit()

try:
    submit_button = driver.find_element('name', 'formTurma:j_id_jsp_1370969402_11')
    submit_button.click()
except NoSuchElementException as e:
    if 'formTurma:j_id_jsp_1370969402_11' in str(e):
        print("Submit element not found")

# Mostra o codigo HTML da página no terminal
# print(driver.page_source)

# Impede que o navegador feche para fins de teste
while(True):
    pass
