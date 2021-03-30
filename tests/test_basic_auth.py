from browser.browser_helper import open_browser
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# Заходим на страницу Basic Auth
driver = open_browser(path="basic_auth")

# Позитивный сценарий с проверкой:
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
body = driver.find_element_by_css_selector('div.example:nth-child(1) p')
assert body.text == "Congratulations! You must have the proper credentials."

# TODO
time.sleep(3)
driver.quit()
driver = open_browser(path="basic_auth")
time.sleep(2)
