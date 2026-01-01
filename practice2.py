'''
Use Playwright to automate the login process on the OrangeHRM demo site.
1. open a page
2. type login credentials
3. click login button
'''
from playwright.sync_api import sync_playwright

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded")

    username = page.wait_for_selector('input[name="username"]')
    username.type("Admin")

    password = page.wait_for_selector('input[name="password"]') 
    password.type("admin123")

    login_button = page.wait_for_selector('button[type="submit"]')
    login_button.click()

    page.wait_for_timeout(5000)
    browser.close()
