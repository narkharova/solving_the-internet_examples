from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pytest


@pytest.mark.parametrize('path', ["horizontal_slider"])
def test_horizontal_slider(driver):
    # Кликаем на слайдер и проверяем значения
    focus = driver.find_element_by_css_selector('input[type=range]')
    focus.click()
    span = driver.find_element_by_css_selector('#range:nth-child(2)')
    assert span.text == "2.5"

    # Перетскиваем слайдер мышкой
    time.sleep(1)
    action = ActionChains(driver)
    action.move_to_element_with_offset(focus, 100, 0).click().perform()
    assert span.text == "4"

    # Перетаскиваем слайддер клавишами
    time.sleep(1)
    focus.send_keys(Keys.ARROW_LEFT)
    assert span.text == "3.5"

    time.sleep(1)
    focus.send_keys(Keys.ARROW_DOWN)
    assert span.text == "3"

    time.sleep(1)
    focus.send_keys(Keys.ARROW_RIGHT)
    assert span.text == "3.5"

    time.sleep(1)
    focus.send_keys(Keys.ARROW_UP)
    assert span.text == "4"
