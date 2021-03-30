from browser.browser_helper import open_browser
import time

# Заходим на страницу Checkboxes
driver = open_browser(path="checkboxes")

# Проверяем первый чекбокс
checkbox1 = driver.find_element_by_css_selector('[type=checkbox]')
checked = checkbox1.get_attribute("checked")
assert checked is None

# Проверяем второй чекбокс
checkbox2 = driver.find_element_by_css_selector('[type=checkbox]:nth-child(3)')
checked = checkbox2.get_attribute("checked")
assert checked == "true"


# Проставить галочку в первом чекбоксе и проверить
time.sleep(2)
click_checkbox1 = driver.find_element_by_css_selector("[type=checkbox]")
click_checkbox1.click()
checked = checkbox1.get_attribute("checked")
assert checked == "true"

# Убрать галочку во втором чекбоксе и проверить
click_checkbox2 = driver.find_element_by_css_selector("[type=checkbox]:nth-child(3)")
click_checkbox2.click()
checked = checkbox2.get_attribute("checked")
assert checked is None

driver.quit()
