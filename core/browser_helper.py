from selenium import webdriver
from chromedriver_py import binary_path


class BrowserHelpers:
    def __init__(self):
        self.driver: webdriver = None
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('window-size=1920,1080')
        self.options.add_argument("--disable-extensions")
        self.binary_path = binary_path
        self.base_url = "https://the-internet.herokuapp.com/"

    def open_browser(self):
        self.driver = webdriver.Chrome(options=self.options, executable_path=self.binary_path)
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.quit()
