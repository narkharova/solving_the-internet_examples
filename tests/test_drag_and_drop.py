import os
import time
import pytest


@pytest.mark.parametrize('path', ["drag_and_drop"])
def test_drag_and_drop(driver):
    # Проверяем текст заголовков
    assert driver.find_element_by_css_selector('#column-a > header').text == 'A'
    assert driver.find_element_by_css_selector('#column-b > header').text == 'B'

    # Переходим в папку js_helpers
    os.chdir('../js_helpers')

    # Открываем скрипт для симуляции drad_and_drop
    time.sleep(2)
    with open(os.path.abspath('drag_and_drop_helper.js'), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()

    # Выполняем скрипт
    driver.execute_script(script + "$('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")

    # Проверяем текст заголовков после изменений
    assert driver.find_element_by_css_selector('#column-a > header').text == 'B'
    assert driver.find_element_by_css_selector('#column-b > header').text == 'A'
