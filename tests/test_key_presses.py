from browser.browser_helper import open_browser
from selenium.webdriver.common.keys import Keys
import time

# Заходим на страницу Key Presses
driver = open_browser(path="key_presses")

# Задаем значение 'D' в поле и проверяем результат
target = driver.find_element_by_css_selector('#target')
target.send_keys('D')
result = driver.find_element_by_css_selector('#result')
assert result.text == "You entered: D"
time.sleep(1)

# Задаем значение "NUMPAD5" в поле и проверяем результат
target.send_keys(Keys.NUMPAD5)
assert result.text == "You entered: NUMPAD5"
time.sleep(1)

# Задаем значение "BACKSPACE" в поле и проверяем результат
target.send_keys(Keys.BACKSPACE)
assert result.text == "You entered: BACK_SPACE"
time.sleep(1)

# Задаем значение "ARROW_UP" в поле и проверяем результат
target.send_keys(Keys.ARROW_UP)
assert result.text == "You entered: UP"
time.sleep(1)

driver.quit()
