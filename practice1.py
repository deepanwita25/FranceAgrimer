from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page= browser.new_page()
    page.goto("https://demo.automationtesting.in/Index.html", wait_until="domcontentloaded")

    # To implemennt a CSS Selector: 3 ways id, class, attribute
    # Using ID - #
    # classname - .
    # attribute - tagname[attribute='value']

    # 1. How to use a CSS Selector - id
    email_textbox = page.wait_for_selector("#email")
    email_textbox.type("test@gmail.com")

    # Click the arrow button to go to login page
    buttonlogin = page.wait_for_selector("#enterimg")
    buttonlogin.click()

    page.wait_for_timeout(5000)
    browser.close()
