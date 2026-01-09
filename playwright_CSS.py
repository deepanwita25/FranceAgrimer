from playwright.sync_api import sync_playwright

""" 
CSS works based on DOM. Can locate elements based on:
1. id
2. class
3. attribute 
"""

"""
When working with CSS selectors, we can use:
1. tag id ->              tag#id
2. tag class ->           tag.class
3. tag attribute ->       tag[attribute='value']
4. tag class attribute -> tag.class[attribute='value']

"""

url = r"https://demowebshop.tricentis.com/" 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded")

    # To locate a web element playwright has provided a method called locator()
    ## 1. tag id -> tag_name#id_value
    search_box = page.locator("input#small-searchterms")
    search_box.fill("T-shirts")
    page.wait_for_timeout(5000)

    browser.close()
    