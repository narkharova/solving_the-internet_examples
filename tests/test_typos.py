import pytest


@pytest.mark.parametrize('path', ["typos"])
def test_typos(driver):
    selector = '#content > div > p:nth-child(3)'
    typo = driver.find_element_by_css_selector(selector)

    while typo.text == "Sometimes you'll see a typo, other times you won,t.":
        driver.refresh()
        typo = driver.find_element_by_css_selector(selector)

    assert typo.text == "Sometimes you'll see a typo, other times you won't."
