import time
import pytest


@pytest.mark.parametrize('path', ["checkboxes"])
def test_checkboxes(driver):
    # Проверяем первый чекбокс
    checkbox1 = driver.find_element_by_css_selector('[type=checkbox]')
    checked = checkbox1.get_attribute("checked")
    assert checked is None

    # Проверяем второй чекбокс
    checkbox2 = driver.find_element_by_css_selector('[type=checkbox]:nth-child(3)')
    checked = checkbox2.get_attribute("checked")
    assert checked == "true"

    # Проставляем галочку в первом чекбоксе и проверяем
    time.sleep(2)
    click_checkbox1 = driver.find_element_by_css_selector("[type=checkbox]")
    click_checkbox1.click()
    checked = checkbox1.get_attribute("checked")
    assert checked == "true"

    # Убраем галочку во втором чекбоксе и проверяем
    click_checkbox2 = driver.find_element_by_css_selector("[type=checkbox]:nth-child(3)")
    click_checkbox2.click()
    checked = checkbox2.get_attribute("checked")
    assert checked is None
