from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://bing.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.keyboard.press("Enter")
    print(page.title())
    browser.close()
