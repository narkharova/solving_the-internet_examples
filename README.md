# solving_the-internet_examples
Проект для изучения Selenium WebDriver. 

Требования находятся в файле requirements.txt:
selenium
chromedriver-py==90.0.4430.24
requests
pytest
PIL

Использовала Chromedriver, Chrome версии 90.0.4430.212. 

Написала UI-автотесты на сайт https://the-internet.herokuapp.com/.
Автотесты находятся в папке tests.
Скриншот тесты в tests/screenshot. 
Пример автотеста с испольованием js-скрипта test_drag_and_drop.py.
Примеры автотестов со скачиванием файлов test_download_secure.py и test_file_downloader.py. 

Тесты на API https://petstore.swagger.io/.
Автотесты на API находятся в папке api_tests.


Запуск
git clone https://github.com/narkharova/solving_the-internet_examples.git
cd solving_the-internet_examples
или 
открыть проект в PyCharm
создать виртуальное окружение
установить модули из requirements.txt.
запустить тесты через терминал pytest tests или PyCharm. 
