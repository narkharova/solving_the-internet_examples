from browser.browser_helper import open_browser
import os
import time

# Заходим на страницу File Uploader
driver = open_browser(path="upload")

# Нажимаем на Upload без файла
button_upload = driver.find_element_by_css_selector('#file-submit').click()
upload_error = driver.find_element_by_css_selector('h1')
assert upload_error.text == "Internal Server Error"
time.sleep(1)

driver.quit()

# Открываем повторно страницу и загружаем файл из папки
driver = open_browser(path="upload")

file_upload = driver.find_element_by_css_selector('#file-upload')
os.chdir('..')
file_upload.send_keys(os.getcwd()+'\\upload\\example')

button_upload = driver.find_element_by_css_selector('#file-submit').click()

# Сравниваем текст загруженного файла
file_uploated = driver.find_element_by_css_selector('#uploaded-files')
assert file_uploated.text == "example"
time.sleep(1)

driver.quit()
