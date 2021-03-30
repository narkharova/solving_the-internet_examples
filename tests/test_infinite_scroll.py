from browser.browser_helper import open_browser

# Заходим на страницу Infinite Scroll
driver = open_browser(path="infinite_scroll")

# Скролим страницу до 1000 раз
i = 0
while i < 1000:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1

# Сверяем кол-во проскроленных абзацев
jscroll = driver.find_elements_by_css_selector(".jscroll-added")
amount = len(jscroll)
assert amount in range(18, 23)

driver.quit()
