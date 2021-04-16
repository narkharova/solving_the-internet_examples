import time
from browser.browser_helper import open_browser

# Заходим на страницу Slow Resources
driver = open_browser(path="slow")
slow_request = []

# Функция для получения запроса slow_external из network
def get_request():
    test = driver.execute_script(
        "var performance = window.performance || {}; var network = performance.getEntries() || {}; return network;")

    for item in range(len(test)):
        if 'slow_external' in test[item]['name']:
            slow_request.append(test[item])

    return slow_request

# Смотрим есть ли запросы slow_request до истечения 30 секунд
slow_request = get_request()

assert len(slow_request) == 0

# Смотрим есть ли запросы slow_request после истечения 30 секунд
time.sleep(33)
slow_request = get_request()

assert len(slow_request) == 1

driver.quit()
