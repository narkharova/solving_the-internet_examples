from selenium.webdriver.common.keys import Keys
import time
import pytest


@pytest.mark.parametrize('path', ["inputs"])
def test_inputs(driver):
    # Задаем значение в поле
    input = driver.find_element_by_css_selector('input[type=number]')
    input.send_keys('8')

    # Меняем значение клавишами
    time.sleep(1)
    input.send_keys(Keys.ARROW_DOWN)
    assert (input.get_attribute('value')) == "7"

    time.sleep(1)
    input.send_keys(Keys.ARROW_UP)
    assert (input.get_attribute('value')) == "8"

    # Проверка больших чисел
    time.sleep(1)
    input.clear()
    input.send_keys('45845641515645644777')
    input.send_keys(Keys.ARROW_DOWN)
    assert (input.get_attribute('value')) == "4.58456415156456447e+19"
