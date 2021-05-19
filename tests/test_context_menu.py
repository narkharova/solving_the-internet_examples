from selenium.webdriver import ActionChains
import pytest


@pytest.mark.parametrize('path', ["context_menu"])
def test_context_menu(driver):
    # Задаём координаты курсора
    action = ActionChains(driver)
    action.move_by_offset(550, 250).context_click().perform()

    # Проверить текст из alert и нажать OK
    alert = driver.switch_to.alert

    assert alert.text == 'You selected a context menu'
    alert.accept()
