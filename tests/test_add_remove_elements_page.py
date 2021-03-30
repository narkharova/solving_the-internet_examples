from browser.browser_helper import open_browser


# Заходим на страницу Add/Remove Elements
driver = open_browser(path="add_remove_elements/")

# Ищем кнопку Add Element
add_button = driver.find_element_by_css_selector("button")

# Нажимаем на неё 100 раз
for count in range(100):
    add_button.click()

# Ищем кнопки Delete и проверяем кол-во =100
del_buttons = driver.find_elements_by_class_name('added-manually')
assert (len(del_buttons)) == 100

# Нажимаем кнопки Delete
for button in range(len(del_buttons)):
    del_buttons[button].click()

# Проверяем возможность добавления новых кнопок после удаления
for count in range(5):
    add_button.click()

del_buttons = driver.find_elements_by_class_name('added-manually')
assert (len(del_buttons)) == 5

driver.quit()
