'''
Relationship between browser, coontext and page in Playwright
'''

# Browser is an interface to browse pages
# browser --> context (user profiles) --> pages
# A browser can have multiple contexts
# A context can have multiple pages

from playwright.sync_api import sync_playwright, expect, Page

URL = "https://visionet.franceagrimer.fr/pages/Statistiques.aspx?menuurl=Statistiques/contexte%20economique/consommation/achats%20des%20m%C3%A9nages/produits%20laitiers"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # Create a new browser context (like a new user profile)
    context = browser.new_context()
    # Can create multiple contexts here if needed
    # context2 = browser.new_context()

    # Create a new page in the context
    page = context.new_page()
    page.goto(URL, wait_until="domcontentloaded")

    page.wait_for_timeout(5000)  # wait for 5 seconds to see the loaded page

    page.wait_for_selector('img.opendoc[telecharger="oui"]')
    download_icons = page.locator('img.opendoc[telecharger="oui"]')
    count = download_icons.count()

    print("Number of download icons found:", count)

    browser.close()

    
