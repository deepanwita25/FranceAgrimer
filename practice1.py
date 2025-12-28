from playwright.sync_api import sync_playwright

""" this code just opens a browser, navigates to a URL, and prints the page title. """

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # Open a new page
    page = browser.new_page()

    # Navigate to the desired URL
    page.goto("https://quotes.toscrape.com/", wait_until ="domcontentloaded")

    # Extract and print the page title
    print("Page Title:", page.title())

    # Close the browser
    browser.close()