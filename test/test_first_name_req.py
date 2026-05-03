def test_first_name_required(page):
    page.goto("https://buggy.justtestit.org/")
    page.click("//a[text()='Register']")

    # Enter all fields except First Name
    page.fill("//input[@name='username']", "testuser123")
    page.fill("//input[@name='lastName']", "Sarathe")
    page.fill("//input[@name='password']", "Password123!")
    page.fill("//input[@name='confirmPassword']", "Password123!")

    # Click Submit
    page.click("//button[@type='submit']")

    # Assert First Name required error appears
    assert page.is_visible("//label[text()='First Name']//following::div[contains(text(),'First Name is required')]")
