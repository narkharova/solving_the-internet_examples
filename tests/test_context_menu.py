from browser.browser_helper import open_browser
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Заходим на страницу Context Menu
driver = open_browser(path="context_menu")

# Задаём координаты курсора
action = ActionChains(driver)
action.move_by_offset(150, 200).context_click().perform()

# Проверить текст из alert и нажать OK
alert = driver.switch_to.alert

assert alert.text =='You selected a context menu'
alert.accept()

time.sleep(3)
driver.quit()
driver = open_browser(path="context_menu")

# # TODO Проверить возможность вызвать ещё раз alert после закрытия
# action.move_by_offset(50, 200).context_click().perform()
