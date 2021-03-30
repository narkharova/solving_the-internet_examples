from browser.browser_helper import open_browser

# Заходим на страницу Large & Deep DOM
driver = open_browser(path="large")

# Находим строки в Siblings и склалдываем числа
sibling_1 = driver.find_element_by_css_selector('#sibling-27\.2').text
assert sibling_1 == "27.2"
sibling_2 = driver.find_element_by_css_selector('#sibling-43\.3').text
assert sibling_2 == "43.3"

assert (float(sibling_1) + (float(sibling_2))) == 70.5

# Находим строки в Table и склалдываем числа
table_1 = driver.find_element_by_css_selector('tr.row-5 > td.column-13').text
assert table_1 == "5.13"
table_2 = driver.find_element_by_css_selector('tr.row-18 > td.column-20').text
assert table_2 == "18.20"

assert (float(table_1) + (float(table_2))) == 23.33

driver.quit()
