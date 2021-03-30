from browser.browser_helper import open_browser
import time

# Заходим на страницу Typos
driver = open_browser(path="typos")

typo = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')

while typo.text == "Sometimes you'll see a typo, other times you won't":
    driver.refresh()

assert typo.text == "Sometimes you'll see a typo, other times you won't"

# TODO 
