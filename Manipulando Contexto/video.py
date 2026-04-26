from playwright.sync_api import sync_playwright
from time import sleep


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(   # grava video e armazena no diretorio
        color_scheme='dark',
        record_video_dir='.',
    )
    page = context.new_page()
    page.goto('http://playwright.dev')
    print(page.title())

    sleep(3)

    browser.close()
