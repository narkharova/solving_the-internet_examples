import time
import pytest


@pytest.mark.parametrize('path', ["hovers"])
def test_hovers(driver):
    driver.find_element_by_css_selector("div:nth-child(5) > img").click()
    time.sleep(2)
    user = driver.find_element_by_css_selector("div:nth-child(5) > div > h5")
    assert user.text == 'name: user3'
    view = driver.find_elements_by_css_selector('a[href^="/"]')

    assert view[2].is_displayed() is True
    assert view[1].is_displayed() is False
    assert view[0].is_displayed() is False
