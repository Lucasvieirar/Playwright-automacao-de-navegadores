from playwright.sync_api import sync_playwright
from time import sleep


with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(   # manipulaando o contexto e abrindo no modo dark
        color_scheme='dark',
    )
    page = context.new_page()
    page.goto('http://playwright.dev')  # site que eu quero 
    print(page.title())

    sleep(3)
 
    browser.close()
