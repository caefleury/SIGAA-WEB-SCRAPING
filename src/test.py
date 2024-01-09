"""
Module: test_retrieve_courses

This module contains a unit test class, TestRetrieve, that tests the functionality
of retrieving coursesfrom the SIGAA platform
for a specific department, year, and term using Selenium.

Dependencies:
- unittest
- json
- selenium.webdriver
- selenium.common.exceptions
- utils.utils (custom utility functions)

Tested Scenario:
- The 'test_retrieve_math_2023_4' method tests the retrieval of courses
  from the Mathematics department for the academic year 2023, term 4.
  It provides expected course data and asserts the results after
  interacting with the SIGAA platform.

Usage:
- To run the tests, execute this module directly or use a testing framework that discovers and runs
  the unit tests.

Example:
    python3 test_retrieve_courses.py

"""

import unittest
import json

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from utils.utils import fill_select, fill_input, form_submit, button_click, retrieve_courses


class TestRetrieve(unittest.TestCase):
    """
    Unit test class for the retrieval of courses from the SIGAA platform.

    This class contains a test case 'test_retrieve_math_2023_4'
    that checks if the course retrieval for the Mathematics department
    in the academic year 2023, term 4, is functioning as expected.

    """

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
                     'expected_courses': [{'course_name': 'ANALISE 1',
                                           'course_code': 'MAT0045',
                                           'course_number': '01',
                                           'anoPeriodo': '2023.4',
                                           'professor': 'RICARDO RUVIARO (30h)\nMARCELO FERNANDES FURTADO (30h)',
                                           'horario': '23456N123',
                                           'vagas_ofertadas': '50',
                                           'vagas_ocupadas': '50',
                                           'local': 'ICC AT-427/10 (Térreo do MAT)'},
                                          {'course_name': 'CÁLCULO 1 - SEMIPRESENCIAL',
                                           'course_code': 'MAT0137',
                                           'course_number': '03',
                                           'anoPeriodo': '2023.4',
                                           'professor': 'ALANCOC DOS SANTOS ALENCAR (60h)\nALINE GOMES DA SILVA PINTO (30h)',
                                           'horario': '7M12345 246N123 35N1234',
                                           'vagas_ofertadas': '71',
                                           'vagas_ocupadas': '70',
                                           'local': 'ICC ANF 12'}]}

        try:
            with open('./data/department_list.json', 'r', encoding='utf-8') as json_file:
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
            for i, course in enumerate(result):
                self.assertEqual(
                    course['course_name'],
                    test_data['expected_courses'][i]['course_name'])

        except (NoSuchElementException, WebDriverException) as e:
            self.fail(f"Test failed due to error: {e}")


if __name__ == '__main__':
    unittest.main()
