from browser.browser_helper import open_browser
import time

# Заходим на страницу Shifting Content: List
driver = open_browser(path="shifting_content/list")

# Находим текст и разделяем его по строкам
content = driver.find_element_by_css_selector('.large-6')
result = content.text.split('\n\n')

# Сравнивам текст с каждой строчкой в массиве
def get_positition():
    for count in range(5):
        if 'Important Information You\'re Looking For' in result[count]:
            position = count
            return position

old_position = get_positition()

# Обновляем страницу и сравниваем новое положение текста со старым
driver.refresh()
content = driver.find_element_by_css_selector('.large-6')
result = content.text.split('\n\n')

new_position = get_positition()
assert old_position != new_position

driver.quit()
