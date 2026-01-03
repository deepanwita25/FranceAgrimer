from playwright.sync_api import sync_playwright

url = r"https://demowebshop.tricentis.com/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
    page.goto(url, wait_until='domcontentloaded')
    page.wait_for_timeout(5000)

    # 1. logo (CSS locator)
    page_header = page.locator("img[alt='Tricentis Demo Web Shop']")
    if page_header.is_visible():
        print('Page header is visible')
    else:
        print('Page header is not visible')

    # 2. Capture all computer related products and verify the count
    products = page.locator("h2>a[href*='computer']")
    product_count = products.count()
    print(f'Product count: {product_count}')

    # 3. Name of the 1st product
    # product_first = products.nth(1)
    product_first = products.first
    print(product_first.inner_text())

    # 3. Name of the last product
    # product_last = products.last
    product_last = products.nth(product_count-1)
    print(product_last.inner_text())

    # 3. Name of the last product
    product_nth = products.nth(1) # 0-based index
    print(product_nth.inner_text())

    # Print title of all the products
    # for i in range(product_count):
    #     print(products.nth(i).inner_text())
    print(products.all_text_contents()) # all_text_contexts() provides a list

    # Element 1 in the Follow Us column
    follow_us_first = page.locator('div.column.follow-us>ul>li:first-child')
    print(f"Follow us 1st element: {follow_us_first.text_content()}")

    follow_us = page.locator('div.column.follow-us>ul>li')
    follow_us_count = follow_us.count()
    print(f"last_element: {follow_us.nth(follow_us_count-1).inner_text()}")

    browser.close()
