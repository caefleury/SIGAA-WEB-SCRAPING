"""
Module: utils

This module provides utility functions for interacting with the SIGAA platform using Selenium.
The functions include filling forms, submitting forms, clicking buttons, and retrieving course data.

Dependencies:
- json
- selenium.webdriver.support.ui.Select
- selenium.common.exceptions.NoSuchElementException
- selenium.webdriver.common.by.By

Functions:
- fill_select(driver, tag, attr, value): Fills a select element with the specified value.
- fill_input(driver, tag, attr, value): Clears and fills an input element with the specified value.
- fill_form(driver, edu_lvl, dept, year, term): Fills the search form with the provided values.
- form_submit(driver, tag, attr): Submits a form with the specified tag and attribute value.
- button_click(driver, tag, attr): Clicks a button with the specified tag and attribute value.
- print_page_source(driver): Prints the page source of the current WebDriver instance.
- retrieve_courses(driver): Retrieves course data from the SIGAA platform 
  and returns a list of courses.
- json_write(data, file_name): Writes data to a JSON file with the specified file name.
- csv_write(data, file_name): Writes data to a CSV file with the specified file name.

Usage:
- Import this module and use the provided functions in your Selenium automation scripts.

Example:
    from utils.utils import fill_form, retrieve_courses

    driver = webdriver.Chrome()
    fill_form(driver, 'G', '17', '2023', '4')
    retrieve_courses(driver)
"""
import json

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def fill_select(driver, tag, atribute_value, select_value):
    """
    Locate a select element on the web page and choose an option by its value.

    Args:
        driver (WebDriver): The WebDriver instance.
        tag (str): The HTML tag of the select element.
        attribute_value (str): The value of the attribute used to locate the select element.
        select_value (str): The value of the option to be selected.

    Returns:
        None: No return value.

    Raises:
        NoSuchElementException: If the select element or option is not found.
    """
    try:
        select_element = driver.find_element(tag, atribute_value)
        select = Select(select_element)
        select.select_by_value(select_value)
    except NoSuchElementException as e:
        return e
    return 0


def fill_input(driver, tag, atribute_value, input_value):
    """
    Locate an input element on the web page, clear its contents, and enter new text.

    Args:
        driver (WebDriver): The WebDriver instance.
        tag (str): The HTML tag of the input element.
        attribute_value (str): The value of the attribute used to locate the input element.
        input_value (str): The text to be entered into the input element.

    Returns:
        None: No return value.

    Raises:
        NoSuchElementException: If the input element is not found.
    """
    try:
        input_element = driver.find_element(tag, atribute_value)
        input_element.clear()
        input_element.send_keys(input_value)
    except NoSuchElementException as e:
        return e
    return 0


def fill_form(driver, educational_level, department, year, term):
    """
    Fills the search form with the provided values.

    Args:
        driver: The Selenium WebDriver instance.
        educational_level (str): The educational level value.
        department (str): The department value.
        year (str): The year value.
        term (str): The term value.

    Returns:
        int: Returns 0 on successful form filling.

    Raises:
        NoSuchElementException: If any form element is not found.

    Example:
        fill_form(driver, 'G', '17', '2023', '4')
    """
    try:
        fill_select(driver, 'id', 'formTurma:inputNivel', educational_level)
        fill_select(driver, 'id', 'formTurma:inputDepto', department)
        fill_input(driver, 'id', 'formTurma:inputAno', year)
        fill_select(driver, 'id', 'formTurma:inputPeriodo', term)
    except NoSuchElementException as e:
        return e
    return 0


def form_submit(driver, tag, atribute_value):
    """
    Submits a form with the specified tag and attribute value.

    Args:
        driver (WebDriver): The WebDriver instance.
        tag (str): The HTML tag of the form element.
        attribute_value (str): The value of the attribute used to locate the form element.

    Returns:
        None: No return value.

    Raises:
        NoSuchElementException: If the form element is not found.
    """
    try:
        form_element = driver.find_element(tag, atribute_value)
        form_element.submit()
    except NoSuchElementException as e:
        return e
    return 0


def button_click(driver, tag, atribute_value):
    """
    Clicks a button with the specified tag and attribute value.

    Args:
        driver (WebDriver): The WebDriver instance.
        tag (str): The HTML tag of the button element.
        attribute_value (str): The value of the attribute used to locate the button element.

    Returns:
        None: No return value.

    Raises:
        NoSuchElementException: If the button element is not found.
    """

    try:
        button_element = driver.find_element(tag, atribute_value)
        button_element.click()
    except NoSuchElementException as e:
        return e
    return 0


def retrieve_courses(driver):
    """
    Retrieves course data from the SIGAA platform and returns a list of courses.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        list: A list containing dictionaries with course information.
    """
    courses = []
    count = 1
    course = {}
    while True:
        try:
            tr = driver.find_element(
                By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]")
        except NoSuchElementException:
            courses.append(course)
            break
        if tr.get_attribute('class') == 'agrupador':
            courses.append(course)
            course = {}
            name = tr.find_element(By.CLASS_NAME, "tituloDisciplina").text
            course_name = name.split(' - ', 1)[1]
            course_code = name.split()[0]
            course['course_name'] = course_name
            course['course_code'] = course_code
        else:
            course['course_number'] = tr.find_element(
                By.CLASS_NAME, "turma").text
            course['anoPeriodo'] = tr.find_element(
                By.CLASS_NAME, "anoPeriodo").text
            course['professor'] = tr.find_element(By.CLASS_NAME, "nome").text
            course['horario'] = driver.find_element(
                By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[4]").text
            course['vagas_ofertadas'] = driver.find_element(
                By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[6]").text
            course['vagas_ocupadas'] = driver.find_element(
                By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[7]").text
            course['local'] = driver.find_element(
                By.XPATH, f"//div[@id='turmasAbertas']/table/tbody/tr[{count}]/td[8]").text
        count += 1

    return courses[1:]


def json_write(data, file_name):
    """
    Writes data to a JSON file with the specified file name.

    Args:
        data: The data to be written to the file.
        file_name (str): The name of the JSON file.

    Returns:
        str: The file path of the created JSON file.
    """
    with open(f'{file_name}', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)
    return 0


def csv_write(data, file_name):
    """
    Writes data to a CSV file with the specified file name.

    Args:
        data: The data to be written to the file.
        file_name (str): The name of the CSV file.

    Returns:
        str: The file path of the created CSV file.
    """
    with open(f'./data/{file_name}.csv', 'w', encoding='utf-8') as csv_file:
        csv_file.write(
            'class_name,class_code,class_number,anoPeriodo,professor,horario,vagas_ofertadas,vagas_ocupadas,local\n') # pylint: disable=line-too-long
        for course in data:
            csv_file.write(
                f"{course['class_name']},{course['class_code']},{course['class_number']},{course['anoPeriodo']},{course['professor']},{course['horario']},{course['vagas_ofertadas']},{course['vagas_ocupadas']},{course['local']}\n") # pylint: disable=line-too-long
    return 0
