import pytest


@pytest.mark.parametrize('path', ["windows"])
def test_windows(driver):
    click_here = driver.find_element_by_css_selector("a[href='/windows/new']").click()

    tabs = driver.window_handles
    assert len(tabs) == 2