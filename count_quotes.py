from playwright.sync_api import sync_playwright

'''
Reference Link: 
https://medium.com/@benawk/clicking-buttons-and-navigating-pages-with-python-playwright-6ef7d723d0f2
'''

def count_quotes_on_page(page):
    quotes = page.locator(".quote")
    return quotes.count()

def click_next_button(page):
    next_button = page.locator("li.next > a")
    next_button.click()
    page.wait_for_load_state("domcontentloaded")


def main():
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/", wait_until="domcontentloaded")
        
        page_number = 1

        while True:
            count_quotes = count_quotes_on_page(page)
            print(f"Page {page_number} has {count_quotes} quotes.")
            next_button = page.locator("li.next > a")
            print(f"Next button count: {next_button.count()}")
            if next_button.count() == 0:
                print("No more pages to navigate. Exiting.")
                break
            prev_url = page.url
            click_next_button(page)
            page.wait_for_function("prev => window.location.href !== prev", arg=prev_url)
            

            page_number = page_number+1
        browser.close()



if __name__ == "__main__":
    main()