from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json
from utils import fill_select,fill_input,form_submit,button_click

# Dados do departamento
with open('./data/depto_data.json', 'r') as json_file:
    depto_data = json.load(json_file)


# Defina a URL que você quer acessar
URL ='https://sigaa.unb.br/sigaa/public/turmas/listar.jsf'

# Defia os inputs da busca
nivel = 'G'
depto = depto_data[17]['value'] # 30 = Computação  , 17 = Matemática
ANO = '2024'
PERIODO = '1'

# Inicie o navegador
driver = webdriver.Chrome() # ou webdriver.Firefox(), dependendo do seu navegador

# Acesse a página
driver.get(URL)
print(json)

fill_select(driver,'id', 'formTurma:inputNivel', nivel)
fill_select(driver,'id', 'formTurma:inputDepto', depto)
fill_input(driver,'id', 'formTurma:inputAno', ANO)
fill_select(driver,'id', 'formTurma:inputPeriodo', PERIODO)

# Submeta o formulário
form_submit(driver,'id', 'formTurma')
button_click(driver,'name', 'formTurma:j_id_jsp_1370969402_11')

# Mostra o codigo HTML da página no terminal
# print(driver.page_source)
        
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

# Impede que o navegador feche para fins de teste
while(True):
    pass
