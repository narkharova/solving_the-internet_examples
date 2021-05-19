import time
import pytest


@pytest.mark.parametrize('path', ["javascript_alerts"])
def test_javascript_alerts(driver):
    # Проверяем текст из alert
    js_alert = driver.find_element_by_css_selector('[onclick="jsAlert()"]').click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert"

    # Нажимаем OK в alert, сравниваем с результатами
    alert.accept()
    result = driver.find_element_by_css_selector('#result')
    assert result.text == "You successfully clicked an alert"
    time.sleep(1)

    # Проверяем текст из confirm
    js_confirm = driver.find_element_by_css_selector('[onclick="jsConfirm()"]')
    js_confirm.click()
    confirm = driver.switch_to.alert
    assert confirm.text == "I am a JS Confirm"

    # Нажимаем OK в confirm, сравниваем с результатом
    alert.accept()
    assert result.text == "You clicked: Ok"
    time.sleep(2)

    # Нажимаем Сancel в confirm, сравниваем с результатом
    js_confirm.click()
    confirm.dismiss()
    assert result.text == "You clicked: Cancel"
    time.sleep(2)

    # Проверяем текст из prompt
    js_prompt = driver.find_element_by_css_selector('[onclick="jsPrompt()"]')
    js_prompt.click()
    prompt = driver.switch_to.alert
    assert prompt.text == "I am a JS prompt"

    # Отправляем текст и нажимаем OK в prompt, сравниваем с результатом
    prompt.send_keys("Yes")
    prompt.accept()
    assert result.text == "You entered: Yes"
    time.sleep(2)

    # Нажимаем Сancel в prompt, сравниваем с результатом
    js_prompt.click()
    prompt.dismiss()
    assert result.text == "You entered: null"
    time.sleep(2)
