import os
import time
import pytest


@pytest.mark.parametrize('path', ["upload"])
def test_upload(driver):
    # Нажимаем на Upload без файла
    driver.find_element_by_css_selector('#file-submit').click()
    upload_error = driver.find_element_by_css_selector('h1')
    assert upload_error.text == "Internal Server Error"
    time.sleep(1)

    driver.quit()

    # Открываем повторно страницу и загружаем файл из папки
    driver.get("https://the-internet.herokuapp.com/upload")

    file_upload = driver.find_element_by_css_selector('#file-upload')
    os.chdir('..')
    file_upload.send_keys(os.getcwd()+'\\upload\\example')

    driver.find_element_by_css_selector('#file-submit').click()

    # Сравниваем текст загруженного файла
    file_uploaded = driver.find_element_by_css_selector('#uploaded-files')
    assert file_uploaded.text == "example"
    time.sleep(1)
