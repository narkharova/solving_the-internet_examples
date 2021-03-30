from browser.browser_helper import open_browser
import time

# Заходим на страницу Login Page
driver = open_browser(path="login")

# Вводим неверный данные на вход
username = driver.find_element_by_css_selector('[name=username]')
password = driver.find_element_by_css_selector('[name=password]')

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

# Проверяем текст alert и перелогиниваемся
login = driver.find_element_by_css_selector('.fa')
login.click()

alert = driver.find_element_by_css_selector('#flash')
assert alert.text == "You logged into a secure area!\n×"
logout = driver.find_element_by_css_selector('.icon-2x').click()


# TODO Вводим неверный логин
username.send_keys("tomsmith1")
password.send_keys("SuperSecretPassword!")
login.click()









