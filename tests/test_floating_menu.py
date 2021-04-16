from browser.browser_helper import open_browser
import time

# Заходим на страницу Floating Menu
driver = open_browser(path="floating_menu")

# Находим кнопки меню
home_button = driver.find_element_by_css_selector('a[href="#home"]')
news_button = driver.find_element_by_css_selector('a[href="#news"]')
contact_button = driver.find_element_by_css_selector('a[href="#contact"]')
about_button = driver.find_element_by_css_selector('a[href="#about"]')

# Скролим страницу вниз
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Проверяем, что кнопки меню остались на месте
home_button.is_displayed()
news_button.is_displayed()
contact_button.is_displayed()
about_button.is_displayed()

time.sleep(2)
driver.quit()
