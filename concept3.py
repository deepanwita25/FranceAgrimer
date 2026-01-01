from playwright.sync_api import sync_playwright

url = "https://quotes.toscrape.com/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded")

    results = []
    quotes = page.locator(".quote")
    count = quotes.count()
    print(f"Total quotes found: {count}")

    for i in range(count):
        quote = quotes.nth(i)
        quote_text = quote.locator(".text").inner_text()
        quote_author = quote.locator(".author").inner_text()
        results.append({"quote": quote_text, "author": quote_author})

    print(f"Extracted {len(results)} quotes")
    print(f"Sample first quote: {results[0]}")
    print(f"Sample last quote: {results[-1]}")
    browser.close()

