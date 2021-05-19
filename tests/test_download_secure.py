# import os
# from selenium import webdriver
# from chromedriver_py import binary_path
# import time
#
# op = webdriver.ChromeOptions()
#
# # Выбираем папку для скачивания
# os.chdir('../temp')
# path = os.getcwd()
# p = {"download.default_directory": path}
#
# # Заходим на страницу Secure File Downloader
# op.add_experimental_option("prefs", p)
# driver = webdriver.Chrome(executable_path=binary_path, options=op)
# driver.implicitly_wait(0.4)
# driver.get("http://admin:admin@the-internet.herokuapp.com/download_secure")
#
# # Скачиваем файлы начинающиеся на "download/"
# links = driver.find_elements_by_css_selector('a[href^="download"]')
# for count in range(len(links)):
#     links[count].click()
#
# # Проверям кол-во скаченных файлов с кол-вом в папке
# filelist = [f for f in os.listdir(path)]
# assert len(filelist) == len(links)
#
# driver.quit()
#
# # Чистим папку temp после выполнения тестов
# time.sleep(3)
# for f in filelist:
#     os.remove(os.path.join(path, f))
#
# #TODO
