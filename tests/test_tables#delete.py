from browser.browser_helper import open_browser

# Заходим на страницу Data Tables
driver = open_browser(path="tables#delete")

table1_elems = driver.find_elements_by_css_selector('#table1 tr')

def find_elems(input):
    for elem in range(len(table1_elems)):
        if input in table1_elems[elem].text:
            return (table1_elems[elem].text)

result = find_elems("Smith")
assert result == "Smith John jsmith@gmail.com $50.00 http://www.jsmith.com edit delete"

result = find_elems("Bach")
assert result == "Bach Frank fbach@yahoo.com $51.00 http://www.frank.com edit delete"

result = find_elems("Nick")
assert result is None

driver.quit()