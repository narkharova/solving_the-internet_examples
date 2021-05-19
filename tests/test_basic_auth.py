import pytest


@pytest.mark.parametrize('path', ["basic_auth"])
def test_basic_auth(driver):
    # Проверка
    driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    body = driver.find_element_by_css_selector('div.example:nth-child(1) p')
    assert body.text == "Congratulations! You must have the proper credentials."
