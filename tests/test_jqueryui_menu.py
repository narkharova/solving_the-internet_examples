import time
import pytest


@pytest.mark.parametrize('path', ["jqueryui/menu"])
def test_jqueryui_menu(driver):
    # Проверяем некликабельность окна меню Disabled
    disabled_button = driver.find_element_by_css_selector('.ui-state-disabled')
    assert 'disabled' in disabled_button.get_attribute('class')

    # Нажимаем на окно меню Enabled
    enabled_button = driver.find_element_by_css_selector('#ui-id-3 > a')
    enabled_button.click()
    time.sleep(1)

    # Нажимаем на окно меню Downloads
    downloads_button = driver.find_element_by_css_selector('#ui-id-4 > a')
    downloads_button.click()
    time.sleep(1)

    # Скачиваем файл PDF
    file_pdf = driver.find_element_by_css_selector('#ui-id-5 > a')
    file_pdf.click()
    time.sleep(2)
