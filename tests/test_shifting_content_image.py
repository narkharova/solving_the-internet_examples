import os
from PIL import Image
from PIL import ImageChops
import pytest


@pytest.mark.parametrize('path', ["shifting_content/image?pixel_shift=500"])
def test_shifting_content_image(driver):
    # Переходим в папку images где лежит референс
    os.chdir('../images')

    # Сделаю референс (только один раз)
    # driver.save_screenshot(название референса)

    # Проверяю картинку при первом заходе на страницу
    driver.save_screenshot("candidate_image.png")

    reference = Image.open("reference_shifting_image.png").convert('RGB')
    candidate = Image.open("candidate_image.png").convert('RGB')

    diff = ImageChops.difference(candidate, reference)

    if diff.getbbox():
        is_the_same = False
    else:
        is_the_same = True

    assert is_the_same is True


    # Делаем рефреш для сдвига картинки на -500 пикселей
    driver.refresh()

    # Проверяем картинку при втором заходе на страницу с двигом в -500 пикселей
    driver.save_screenshot("candidate_image.png")

    reference = Image.open("reference_shifting_image_500.png").convert('RGB')
    candidate = Image.open("candidate_image.png").convert('RGB')

    diff = ImageChops.difference(candidate, reference)

    if diff.getbbox():
        is_the_same = False
    else:
        is_the_same = True

    assert is_the_same is True
