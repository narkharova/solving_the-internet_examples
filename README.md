# solving_the-internet_examples
Личный проект для изучения Selenium WebDriver. 
Актуален с Chromedriver, Chrome версии 90.0.4430.212.

Написала UI автотесты на сайт https://the-internet.herokuapp.com/.
Тесты на API https://petstore.swagger.io/.

Контакты для связи: natalya.arkharova93@gmail.com

# Содержание проекта
UI Автотесты находятся в папке tests.

Автотесты на API находятся в папке api_tests.

Скриншот тесты в tests/screenshot.

Пример автотеста с использованием js-скрипта: ```test_drag_and_drop.py.```

Примеры автотестов со скачиванием файлов: ```test_download_secure.py, test_file_downloader.py```

# Requirements
Устанавливать из requirements.txt:
```
selenium
chromedriver-py==90.0.4430.24
requests
pytest
Pillow
```

# Запуск
## Запуск через терминал:
1. Клонировать и открыть проект.
```
git clone https://github.com/narkharova/solving_the-internet_examples.git
```
```
cd solving_the-internet_examples
```
2. Создать и войти в виртуальное окружение.
```
pipenv --python 3.9.5
```
```
pipenv shell
```
3. Установить модули из requirements.txt.
```
pip install -r requirements.txt 
```
4. Запустить все тесты.
```
pytest tests
```
5. Запустить один тест.
```
pytest tests/test_login.py
```
```
pytest api_tests/test_api_example.py::test_post_request
```

## Запуск через PyCharm
1. Клонировать и открыть проект.
2. Создать виртуальное окружение. 
3. Установить модули из requirements.txt.
4. Убедиться, что pytest выбран как **Default test runner** в **Settings > Tools > Python Integrated Tools**.
5. Запустить тесты через любую конфигурацию pytest.

# Управление браузером выполняется через класс BrowserHelpers
```
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
```
            self.driver.quit()
