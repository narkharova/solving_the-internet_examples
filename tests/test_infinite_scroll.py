import pytest


@pytest.mark.parametrize('path', ["infinite_scroll"])
def test_infinite_scroll(driver):
    # Скролим страницу до 1000 раз
    i = 0
    while i < 1000:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i = i + 1

    # Сверяем кол-во проскроленных абзацев
    jscroll = driver.find_elements_by_css_selector(".jscroll-added")
    amount = len(jscroll)
    assert amount in range(18, 23)
