from browser.browser_helper import open_browser

# Заходим на страницу Notification Message
driver = open_browser(path="notification_message_rendered")

# Кликаем на новое сообщение и сохраняем первый текст
driver.find_element_by_css_selector('a[href="/notification_message"]').click()

alert = driver.find_element_by_css_selector('[data-alert]')
first_text = alert.text

# Сравниваем первый текст с текущим в цикле
while alert.text == first_text:
    driver.refresh()
    driver.find_element_by_css_selector('a[href="/notification_message"]').click()
    alert = driver.find_element_by_css_selector('[data-alert]')

# Проверяем, что первый текст не равен текущему
assert first_text != alert.text

# Проверяем корректность текстов
assert first_text == "Action successful\n×" or "Action unsuccesful, please try again\n×"
assert alert.text == "Action successful\n×" or "Action unsuccesful, please try again\n×"

driver.quit()
