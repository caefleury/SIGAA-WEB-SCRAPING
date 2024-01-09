import unittest
import json

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from utils.utils import *


class TestRetrieve(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_retrieve_math_2023_4(self):
        """
        Test that it can retrieve courses from the math department in 2023.4

        """

        test_data = {'url': 'https://sigaa.unb.br/sigaa/public/turmas/listar.jsf',
                     'dept_id': 17,
                     'expected_courses': [{'class_name': 'ANALISE 1',
                                           'class_code': 'MAT0045',
                                           'class_number': '01',
                                           'anoPeriodo': '2023.4',
                                           'professor': 'RICARDO RUVIARO (30h)\nMARCELO FERNANDES FURTADO (30h)',
                                           'horario': '23456N123',
                                           'vagas_ofertadas': '50',
                                           'vagas_ocupadas': '50',
                                           'local': 'ICC AT-427/10 (Térreo do MAT)'},
                                          {'class_name': 'CÁLCULO 1 - SEMIPRESENCIAL',
                                           'class_code': 'MAT0137',
                                           'class_number': '03',
                                           'anoPeriodo': '2023.4',
                                           'professor': 'ALANCOC DOS SANTOS ALENCAR (60h)\nALINE GOMES DA SILVA PINTO (30h)',
                                           'horario': '7M12345 246N123 35N1234',
                                           'vagas_ofertadas': '71',
                                           'vagas_ocupadas': '71',
                                           'local': 'ICC ANF 12'}]}

        try:
            with open('./data/dept_data.json', 'r') as json_file:
                dept_data = json.load(json_file)
            self.driver.get(test_data['url'])
            fill_select(self.driver, 'id', 'formTurma:inputNivel', 'G')
            fill_select(
                self.driver,
                'id',
                'formTurma:inputDepto',
                dept_data[17]['value'])
            fill_input(self.driver, 'id', 'formTurma:inputAno', '2023')
            fill_select(self.driver, 'id', 'formTurma:inputPeriodo', '4')
            form_submit(self.driver, 'id', 'formTurma')
            button_click(
                self.driver,
                'name',
                'formTurma:j_id_jsp_1370969402_11')

            result = retrieve_courses(self.driver)

            self.assertEqual(result, test_data['expected_courses'])
            self.assertEqual(len(result), len(test_data['expected_courses']))
            for i in range(len(result)):
                self.assertEqual(
                    result[i]['class_name'],
                    test_data['expected_courses'][i]['class_name'])

        except (NoSuchElementException, WebDriverException) as e:
            self.fail(f"Test failed due to error: {e}")


if __name__ == '__main__':
    unittest.main()
