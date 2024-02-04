# SIGAA-WEB-SCRAPING
O SIGAA-WEB-SCRAPING é um projeto em Python que utiliza a biblioteca Selenium para realizar web scraping na página de turmas da Universidade de Brasília (UnB) na plataforma SIGAA. Este projeto tem como objetivo extrair informações relevantes das turmas oferecidas, possibilitando análises ou automação de processos relacionados.

*Esse projeto também foi usado para estudar modularização e pacotes em python e, portanto, há uma divisão excessiva de funções em
diferentes pastas e arquivos.*

## Requisitos
Antes de começar, certifique-se de ter instalado os seguintes requisitos:

- Python 3.x
- Selenium
- WebDriver (por exemplo, ChromeDriver)

Você pode instalar as dependências executando:

`pip install -r requirements.txt`

## Uso

Execute o script main.py localizado na pasta src para iniciar o processo de web scraping. Certifique-se de ajustar as configurações no código, como URL da página de turmas, seletores e qualquer outra informação específica da busca no arquivo.

`python3 src/main.py`

*No momento a escolha dos departamentos é inteiramente manual e deve ser modificada na variável `decent_department_list`* :sweat_smile:.

```
decent_department_list = [
        {"name": "DEPARTAMENTO DE MATEMÁTICA", "value": "518"},
        # {"name": "DEPARTAMENTO DE CIÊNCIAS DA COMPUTAÇÃO", "value": "508"},
        # {"name": "DEPARTAMENTO DE ENGENHARIA ELÉTRICA", "value": "443"},
    ]
```

## Contribuição
Este projeto serve como um teste inicial para a implementação do gerador de grade utilizando o Selenium e uma framework web como Django ou uma API como o Flask. As melhorias serão realizadas em projetos subsequentes. No entanto, sinta-se à vontade para contribuir com aprimoramentos, correções de bugs ou novos recursos. Abra uma discussão para propor melhorias.
