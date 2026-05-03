class RegisterPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://buggy.justtestit.org/register")

    def enter_username(self, value):
        self.page.fill("//input[@name='username']", value)

    def enter_first_name(self, value):
        self.page.fill("//input[@name='firstName']", value)

    def enter_last_name(self, value):
        self.page.fill("//input[@name='lastName']", value)

    def enter_password(self, value):
        self.page.fill("//input[@name='password']", value)

    def enter_confirm_password(self, value):
        self.page.fill("//input[@name='confirmPassword']", value)

    def click_register(self):
        self.page.click("//button[@type='submit']")
