from browser.browser_helper import open_browser
from selenium.webdriver.common.keys import Keys
import time

# Заходим на страницу Dropdown List
driver = open_browser(path="dropdown")

select = driver.find_element_by_id("dropdown")
select.click()

# Находим текст вариантов селекта
time.sleep(1)
first_option = driver.find_element_by_css_selector('[value="1"]').text
second_option = driver.find_element_by_css_selector('[value="2"]').text

# Нажимаем на клавишу вниз
select.send_keys(Keys.ARROW_DOWN)
select.send_keys(Keys.ENTER)

# Проверяем, что выбрали первый вариант
chosen_value = select.get_attribute('value')
choosen_option_text = driver.find_element_by_css_selector(f'[value="{chosen_value}"]').text

assert choosen_option_text == first_option
assert chosen_value == "1"

driver.quit()

