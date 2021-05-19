import time
import pytest


@pytest.mark.parametrize('path', ["dynamic_controls"])
def test_dynamic_controls(driver):
    # Находим чекбокс и поле для ввода текста
    checkbox = driver.find_element_by_css_selector('[type=checkbox]')
    input = driver.find_element_by_css_selector('input[type=text]')

    # Нажимаем кнопки Remove и Enable
    remove_add = driver.find_element_by_css_selector('#checkbox-example > button')
    remove_add.click()

    enable_disable = driver.find_element_by_css_selector('#input-example > button')
    enable_disable.click()

    # Проверяем загрузку
    checkbox_loading = driver.find_element_by_css_selector('#checkbox-example #loading')
    input_loading = driver.find_element_by_css_selector('#input-example #loading')
    time.sleep(4)

    # Проверяем сообщения после загрузки
    checkbox_message = driver.find_element_by_css_selector('#checkbox-example #message')
    checkbox_message.text == "It's back!"

    input_message = driver.find_element_by_css_selector('#input-example #message')
    input_message.text == "It's enabled!"

    # Вводим данные в поле и нажимаем Disable и Add
    input.send_keys('yes')
    remove_add.click()
    enable_disable.click()
    time.sleep(3)

    # Проверяем, что чекбокс снова появился
    checkbox = driver.find_element_by_css_selector('[type=checkbox]')
    checkbox.is_displayed()
