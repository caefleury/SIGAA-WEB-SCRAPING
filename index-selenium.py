from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url ='https://sigaa.unb.br/sigaa/public/turmas/listar.jsf'
print('here1')
# Inicie o navegador

driver = webdriver.Chrome() # ou webdriver.Chrome(), dependendo do seu navegador
print('here2')
# Acesse a página
driver.get(url)
print('here3')
# Encontre o select
try:
    select_element = driver.find_element_by_id('formTurma:inputNivel')
    # rest of the code
except NoSuchElementException as e:
    print(f"Element not found: {e}")

# Selecione a opção com value='G'
select = Select(select_element)
select.select_by_value('G')

# Submeta o formulário
form_element = driver.find_element_by_name('formTurma')
form_element.submit()



print(driver.page_source)

driver.quit()
# Aguarde a página recarregar e continue com o restante do seu código...