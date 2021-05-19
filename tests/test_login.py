import pytest


def login(driver):
    username = driver.find_element_by_css_selector('[name=username]')
    password = driver.find_element_by_css_selector('[name=password]')
    button_login = driver.find_element_by_css_selector('.fa')
    return username, password, button_login


@pytest.mark.parametrize('path', ["login"])
def test_login(driver):
    # Вводим верный данные на вход
    username, password, button_login = login(driver)

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    button_login.click()

    # Проверяем текст alert и перелогиниваемся
    alert = driver.find_element_by_css_selector('#flash')
    assert alert.text == "You logged into a secure area!\n×"
    logout = driver.find_element_by_css_selector('.icon-2x').click()


    # Вводим неверный логин
    username, password, button_login = login(driver)
    username.send_keys("tomsmith!")
    password.send_keys("SuperSecretPassword!")
    button_login.click()

    # Проверяем текст alert
    alert = driver.find_element_by_css_selector('#flash')
    assert alert.text == "Your username is invalid!\n×"

    # Вводим неверный пароль
    username, password, button_login = login(driver)
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword")
    button_login.click()

    # Проверяем текст alert
    alert = driver.find_element_by_css_selector('#flash')
    assert alert.text == "Your password is invalid!\n×"
