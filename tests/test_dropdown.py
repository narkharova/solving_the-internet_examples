from selenium.webdriver.common.keys import Keys
import time
import pytest


@pytest.mark.parametrize('path', ["dropdown"])
def test_dropdown(driver):
    select = driver.find_element_by_id("dropdown")
    select.click()

    # Находим текст вариантов селекта
    time.sleep(1)
    option = driver.find_element_by_css_selector('[value="1"]').text

    # Нажимаем на клавишу вниз
    select.send_keys(Keys.ARROW_DOWN)
    select.send_keys(Keys.ENTER)

    # Проверяем, что выбрали первый вариант
    chosen_value = select.get_attribute('value')
    chosen_option_text = driver.find_element_by_css_selector(f'[value="{chosen_value}"]').text

    assert chosen_option_text == option
    assert chosen_value == "1"
