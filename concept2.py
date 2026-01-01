from playwright.sync_api import sync_playwright

url = "https://quotes.toscrape.com/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded")

    # Locator: points to all elements with class name 'quote'
    quotes = page.locator(".quote")
    # Count and print the number of quote elements found in page 1
    print("Number of quotes on the page:", quotes.count())

    # Extract and print the quote 1
    first_quote = quotes.first

    # Inside the first quote, find the text and author
    quote_text = first_quote.locator(".text").inner_text()
    quote_author = first_quote.locator(".author").inner_text()

    print({"quote": quote_text, "author": quote_author})

    # Close the browser
    browser.close()