import seleniumpip.webdriver as webdriver

def get_results(search_term):
    url = "https://www.google.com"
    browser = webdriver.Firefox()
    browser.get(url)
    search_box = browser.find_element_by_id("query")
    search_box.send_keys(search_term)
    search_box.submit()
