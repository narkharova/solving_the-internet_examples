from core.browser_helper import BrowserHelpers
import pytest


@pytest.fixture()
def driver(path):
    browser = BrowserHelpers()
    driver = browser.open_browser()
    driver.get(browser.base_url + path)

    yield driver

    browser.close_browser()

    return driver
