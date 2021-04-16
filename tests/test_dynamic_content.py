from browser.browser_helper import open_browser
import time

# Заходим на страницу Dynamic Content
driver = open_browser(path="dynamic_content?with_content=static")

# Находим первый текст
first_elem = driver.find_element_by_css_selector('div:nth-child(1) > div.large-10')
first_elem_text = "Accusantium eius ut architecto neque vel voluptatem vel nam eos minus ullam dolores voluptates enim sed voluptatem rerum qui sapiente nesciunt aspernatur et accusamus laboriosam culpa tenetur hic aut placeat error autem qui sunt."
assert first_elem.text == first_elem_text

# Находим второй текст
second_elem = driver.find_element_by_css_selector('div:nth-child(4) > div.large-10')
second_elem_text = "Omnis fugiat porro vero quas tempora quis eveniet ab officia cupiditate culpa repellat debitis itaque possimus odit dolorum et iste quibusdam quis dicta autem sint vel quo vel consequuntur dolorem nihil neque sunt aperiam blanditiis."
assert second_elem.text == second_elem_text

# Находим третий текст
third_elem = driver.find_element_by_css_selector('#content > div:nth-child(7) > div.large-10')
old_text = third_elem.text

driver.refresh()

# Проверяем после обновления, что первый и второй текст не изменились, третитй изменился
first_elem = driver.find_element_by_css_selector('div:nth-child(1) > div.large-10')
assert first_elem.text == first_elem_text

second_elem = driver.find_element_by_css_selector('div:nth-child(4) > div.large-10')
assert second_elem.text == second_elem_text

third_elem = driver.find_element_by_css_selector('#content > div:nth-child(7) > div.large-10')
assert third_elem.text != old_text

time.sleep(1)
driver.quit()
