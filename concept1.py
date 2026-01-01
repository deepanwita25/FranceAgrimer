from playwright.sync_api import sync_playwright

url = "https://quotes.toscrape.com/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto(url, wait_until ="domcontentloaded")


    # Extract and print the page title
    print("Page Title:", page.title())

    # Close the browser
    browser.close()