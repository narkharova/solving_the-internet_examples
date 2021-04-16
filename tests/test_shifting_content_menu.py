import os
from PIL import Image
from PIL import ImageChops
from browser.browser_helper import open_browser

# Открываем браузер
driver = open_browser('shifting_content/menu?pixel_shift=100')

# Переходим в папку images где лежит референс
os.chdir('../images')

# Сделаю референс (только один раз) driver.save_screenshot("menu_image.png")

# Проверяю картинку при первом заходе на страницу
driver.save_screenshot("new_menu.png")

reference = Image.open("menu_image.png").convert('RGB')
candidate = Image.open("new_menu.png").convert('RGB')

diff = ImageChops.difference(candidate, reference)

if diff.getbbox():
    is_the_same = False
else:
    is_the_same = True

assert is_the_same is True


# Делаю рефреш для сдвига картинки на -100 пикселей
driver.refresh()

# Проверяю картинку при втором заходе на страницу с двигом в -100 пикселей
driver.save_screenshot("new_menu.png")

reference = Image.open("menu_image_100.png").convert('RGB')
candidate = Image.open("new_menu.png").convert('RGB')

diff = ImageChops.difference(candidate, reference)

if diff.getbbox():
    is_the_same = False
else:
    is_the_same = True

assert is_the_same is True

driver.quit()

