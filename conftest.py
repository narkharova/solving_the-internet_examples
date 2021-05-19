from core.browser_helper import open_browser
import pytest


@pytest.fixture()
def driver():
    driver = open_browser(path="add_remove_elements/")
    return driver