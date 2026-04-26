from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    request = p.request.new_context()
    response = request.get('https://dog.ceo/api/breeds/image/random')
    print(response.status)
    print(response.text())
    print(response.json())
