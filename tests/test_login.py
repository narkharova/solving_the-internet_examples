from browser.browser_helper import open_browser

# Заходим на страницу Login Page
driver = open_browser(path="login")

# Вводим верный данные на вход
def login():
    username = driver.find_element_by_css_selector('[name=username]')
    password = driver.find_element_by_css_selector('[name=password]')
    button_login = driver.find_element_by_css_selector('.fa')
    return username, password, button_login

username, password, button_login = login()

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
button_login.click()

# Проверяем текст alert и перелогиниваемся
alert = driver.find_element_by_css_selector('#flash')
assert alert.text == "You logged into a secure area!\n×"
logout = driver.find_element_by_css_selector('.icon-2x').click()


# Вводим неверный логин
username, password, button_login = login()
username.send_keys("tomsmith!")
password.send_keys("SuperSecretPassword!")
button_login.click()

# Проверяем текст alert
alert = driver.find_element_by_css_selector('#flash')
assert alert.text == "Your username is invalid!\n×"

# Вводим неверный пароль
username, password, button_login = login()
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword")
button_login.click()

# Проверяем текст alert
alert = driver.find_element_by_css_selector('#flash')
assert alert.text == "Your password is invalid!\n×"

driver.quit()
