from browser.browser_helper import open_browser
import time

# Заходим на страницу Typos
driver = open_browser(path="typos")

selector = '#content > div > p:nth-child(3)'
typo = driver.find_element_by_css_selector(selector)

while typo.text == "Sometimes you'll see a typo, other times you won,t.":
    driver.refresh()
    typo = driver.find_element_by_css_selector(selector)

assert typo.text == "Sometimes you'll see a typo, other times you won't."

driver.quit()