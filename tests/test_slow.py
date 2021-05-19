import time
import pytest


def get_request(driver):
    slow_request = []

    test = driver.execute_script(
        "var performance = window.performance || {}; var network = performance.getEntries() || {}; return network;")

    for item in range(len(test)):
        if 'slow_external' in test[item]['name']:
            slow_request.append(test[item])

    return slow_request

@pytest.mark.parametrize('path', ["slow"])
def test_slow(driver):


    # Смотрим есть ли запросы slow_request до истечения 30 секунд
    slow_request = get_request(driver)

    assert len(slow_request) == 0

    # Смотрим есть ли запросы slow_request после истечения 30 секунд
    time.sleep(33)
    slow_request = get_request(driver)

    assert len(slow_request) == 1
