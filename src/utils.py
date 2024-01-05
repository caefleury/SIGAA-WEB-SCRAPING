
# Retorna as infromações do departamento atraves do nome
def return_depto_by_name(depto_data, depto_name):
    for depto in depto_data:
        if depto.get('name') == depto_name:
            return depto
    return None