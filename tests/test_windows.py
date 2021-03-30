from browser.browser_helper import open_browser

# Заходим на страницу Opening a new window
driver = open_browser(path="windows")

click_here = driver.find_element_by_css_selector("a[href='/windows/new']").click()

tabs = driver.window_handles
assert len(tabs) == 2