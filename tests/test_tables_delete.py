import pytest


def find_elems(input, table1_elems):
    for elem in range(len(table1_elems)):
        if input in table1_elems[elem].text:
            return (table1_elems[elem].text)


@pytest.mark.parametrize('path', ["tables#delete"])
def test_tables_delete(driver):
    table1_elems = driver.find_elements_by_css_selector('#table1 tr')

    result = find_elems("Smith", table1_elems)
    assert result == "Smith John jsmith@gmail.com $50.00 http://www.jsmith.com edit delete"

    result = find_elems("Bach", table1_elems)
    assert result == "Bach Frank fbach@yahoo.com $51.00 http://www.frank.com edit delete"

    result = find_elems("Nick", table1_elems)
    assert result is None
