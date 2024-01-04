from bs4 import BeautifulSoup
import requests

# Lista de turmas
turmas = []
url ='https://sigaa.unb.br/sigaa/public/turmas/listar.jsf'

# Acesse a página inicial
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Encontre o formulário
form = soup.find('form')
form_data = {}

# Preencha os dados do formulário com os valores atuais
for select in form.find_all('select'):
    # print(select)
    if select.get('id') == 'formTurma:inputNivel':
        option = select.find('option', value='G')
        if option:
            # Adicione ao form_data
            form_data[select.get('name')] = option.get('value')
    
print(form_data)

# Faça a requisição POST com os dados do formulário atualizados
response = requests.post(url, data=form_data)
soup = BeautifulSoup(response.content, "html.parser")

print(soup)
# Atualize a classe do option selecionado
# select = soup.find("select")
# options = select.find_all("option", value="518")

# if options:
#     option = options[0]
#     option['class'] = 'selected'  # Adicione a classe 'selected'
#     form_data[select.get('name')] = option.get('value')




# print(soup)
print(form_data)
# Continue com o restante do seu código...