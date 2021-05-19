import pytest


def get_position(result):
    for count in range(5):
        if 'Important Information You\'re Looking For' in result[count]:
            position = count
            return position


@pytest.mark.parametrize('path', ["shifting_content/list"])
def test_shifting_content_list(driver):
    # Находим текст и разделяем его по строкам
    content = driver.find_element_by_css_selector('.large-6')
    result = content.text.split('\n\n')

    # Сравнивам текст с каждой строчкой в массиве
    old_position = get_position(result)

    # Обновляем страницу и сравниваем новое положение текста со старым
    driver.refresh()
    content = driver.find_element_by_css_selector('.large-6')
    result = content.text.split('\n\n')

    new_position = get_position(result)
    assert old_position != new_position
