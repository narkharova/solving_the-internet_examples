from browser.browser_helper import open_browser
import time

# Заходим на страницу Disappearing Elements
driver = open_browser(path="disappearing_elements")

# Проверяем 4 обязательных элемента
elements = driver.find_elements_by_css_selector('a[href^="/"]')

assert elements[0].text == "Home"
assert elements[1].text == "About"
assert elements[2].text == "Contact Us"
assert elements[3].text == "Portfolio"

# Повторяем цикл, если элементов меньше 5
while len(elements) < 5:
    driver.refresh()
    elements = driver.find_elements_by_css_selector('a[href^="/"]')

assert len(elements) == 5
assert elements[4].text == "Gallery"

time.sleep(2)
driver.quit()


