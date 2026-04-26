from playwright.sync_api import sync_playwright
from time import sleep


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto('https://www.python.org/')

    about_button = page.locator('id=about')

    print(about_button.text_content())
    about_button.click()

    sleep(5)

    browser.close()
