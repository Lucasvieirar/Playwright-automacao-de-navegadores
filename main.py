from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False) 

    page = browser.new_page()

    page.goto('http://playwright.dev') #pagina que eu quero

    print(page.title()) #print no titulo

    browser.close()
