from playwright.sync_api import sync_playwright
from time import sleep


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        color_scheme='dark',
        viewport={'width': 800, 'height': 600},
    )
    page = context.new_page()
    page.goto('http://playwright.dev')
    print(page.title())

    page.screenshot(path='tela.png', type='png')

    sleep(3)

    browser.close()
