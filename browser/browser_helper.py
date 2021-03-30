from selenium import webdriver
from chromedriver_py import binary_path

base_url = "https://the-internet.herokuapp.com/"


def open_browser(path):
    driver = webdriver.Chrome(binary_path)
    driver.get(base_url + path)
    return driver
