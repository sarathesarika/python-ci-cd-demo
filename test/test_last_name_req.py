def test_last_name_required(page):
    page.goto("https://buggy.justtestit.org/")
    page.click("//a[text()='Register']")

    # Enter all fields except Last Name
    page.fill("//input[@name='username']", "testuser456")
    page.fill("//input[@name='firstName']", "Sarika")
    page.fill("//input[@name='password']", "Password123!")
    page.fill("//input[@name='confirmPassword']", "Password123!")

    # Click Submit
    page.click("//button[@type='submit']")

    # Assert Last Name required error
    assert page.is_visible("//label[text()='Last Name']//following::div[contains(text(),'Last Name is required')]")
