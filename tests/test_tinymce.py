from browser.browser_helper import open_browser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException


# Заходим на страницу
driver = open_browser(path="tinymce")

# Находим iframe на странице и переключаемся в него
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

# Берем поле для ввода из фрейма
body = driver.find_element_by_css_selector('[data-id="mce_0"]')

# Переходим на новую строку и пишем Hello
body.send_keys(Keys.ENTER)
body.send_keys('Hello')

# Проверяем что в поле появился текст Hello
assert body.text == 'Your content goes here.\nHello'

# Выходим из фрейма
driver.switch_to.parent_frame()

# Находим и кликаем на кнопку Bold
bold_button = driver.find_element_by_css_selector('[aria-label="Bold"]')
bold_button.click()

# Возвращаемся во фрейм и вводим 'жирный' текст на новой строке
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
body.send_keys(Keys.ENTER)
body.send_keys('Hello')

# Проверяем что появился второй Hello
assert body.text == 'Your content goes here.\nHello\nHello'

# Проверяем что у второго Hello есть тэг strong так как он был введен при включенной кнопке Bold
bold_text = driver.find_element_by_tag_name('strong')

# Выходим из фрейма
driver.switch_to.parent_frame()

# Попытка ввести в элемент фрейма значение, когда уже вышли из фрейма
try:
    body.send_keys('Hello')
except StaleElementReferenceException:
    pass  # в случае ошибки пропустить

driver.quit()
