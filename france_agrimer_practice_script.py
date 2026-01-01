'''
This script demonstrates how to locate web elements using Playwright.
How to locate elements:
1. Playwright built-in locators - Playwright Locators
2. CSS Selectors - Traditional Locators
3. XPath Selectors - Traditional Locators
'''

from playwright.sync_api import sync_playwright
import os

URL = "https://visionet.franceagrimer.fr/pages/Statistiques.aspx?menuurl=Statistiques/contexte%20economique/consommation/achats%20des%20m%C3%A9nages/produits%20laitiers"
download_dir = r"C:\Users\deepa\OneDrive\Learn_playwright\FranceAgrimer"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # ✅ accept_downloads=True is required for downloads
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    page.goto(URL, wait_until="domcontentloaded")

    # wait until at least one telecharger icon exists
    page.wait_for_selector("img.opendoc[telecharger='oui']")

    # On this site, many matches can exist; :visible targets those shown right now
    telecharger = page.locator("img.opendoc[telecharger='oui']:visible")
    n = telecharger.count()
    print("Visible download icons on this page:", n)

    for i in range(n):
        with page.expect_download() as dl_info:
            telecharger.nth(i).click()
        download = dl_info.value
        save_path = os.path.join(download_dir, download.suggested_filename)
        download.save_as(save_path)
        print(f"Downloaded {i+1}/{n}: {download.suggested_filename}")


    browser.close()
