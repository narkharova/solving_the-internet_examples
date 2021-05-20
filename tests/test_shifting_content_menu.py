import os
from PIL import Image
from PIL import ImageChops
import pytest


def make_new_reference(driver):
    driver.save_screenshot("reference_menu.png")


@pytest.mark.parametrize('path', ["shifting_content/menu?pixel_shift=100"])
def test_shifting_content_menu(driver):
    # Переходим в папку images где лежит референс
    os.chdir('../images')

    # Проверяем картинку при первом заходе на страницу
    driver.save_screenshot("candidate_menu.png")

    reference = Image.open("reference_menu.png").convert('RGB')
    candidate = Image.open("candidate_menu.png").convert('RGB')

    diff = ImageChops.difference(candidate, reference)

    if diff.getbbox():
        is_the_same = False
    else:
        is_the_same = True

    assert is_the_same is True


    # Делаем рефреш для сдвига картинки на -100 пикселей
    driver.refresh()

    # Проверяем картинку при втором заходе на страницу с двигом в -100 пикселей
    driver.save_screenshot("candidate_menu_100.png")

    reference = Image.open("reference_menu_100.png").convert('RGB')
    candidate = Image.open("candidate_menu_100.png").convert('RGB')

    diff = ImageChops.difference(candidate, reference)

    if diff.getbbox():
        is_the_same = False
    else:
        is_the_same = True

    assert is_the_same is True
