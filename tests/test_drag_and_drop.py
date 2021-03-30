import os
import time

from browser.browser_helper import open_browser

# Заходим на страницу Drag and Drop
driver = open_browser(path="drag_and_drop")

# Проверяем текст заголовков
assert driver.find_element_by_css_selector('#column-a > header').text == 'A'
assert driver.find_element_by_css_selector('#column-b > header').text == 'B'

# Переходим в папку helpers
os.chdir('../helpers')

# Открываем скрипт для симуляции drad_and_drop
time.sleep(2)
with open(os.path.abspath('drag_and_drop_helper.js'), 'r') as js_file:
    line = js_file.readline()
    script = ''
    while line:
        script += line
        line = js_file.readline()

# Выполняем скрипт
driver.execute_script(script + "$('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")

# Проверяем текст заголовков после изменений
assert driver.find_element_by_css_selector('#column-a > header').text == 'B'
assert driver.find_element_by_css_selector('#column-b > header').text == 'A'
time.sleep(2)

driver.quit()
