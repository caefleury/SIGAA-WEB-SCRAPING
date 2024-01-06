from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
depto = depto_data[17]['value'] # 30 = Computação  , 17 = Matemática
select_depto = Select(select_element_depto)
select_depto.select_by_value(depto)

# Seleciona o ano
ANO = '2023'
input_element_ano.clear() 
input_element_ano.send_keys(ANO)

# Selecione o periodo
PERIODO = '4'
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
