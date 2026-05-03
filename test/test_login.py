def test_login(page):
    # Go to website
    page.goto("https://buggy.justtestit.org/")

    # Click Login button
    page.click("//button[text()='Login']")

    # Enter username
    page.fill("//input[@name='login']", "your_username")

    # Enter password
    page.fill("//input[@type='password']", "your_password")

    # Click Login button again
    page.click("//button[text()='Login']")

    # Add assertion
    assert "buggy" in page.url
