import pytest
from playwright.sync_api import Page
from pages.register_page import RegisterPage


@pytest.mark.usefixtures("browser_page")
class TestRegistration:

    def test_register_success(self, browser_page: Page):
        page = browser_page
        register = RegisterPage(page)

        register.open()
        register.enter_username("testuser12345")
        register.enter_first_name("Shamika")
        register.enter_last_name("S")
        register.enter_password("Testing@123")
        register.enter_confirm_password("Testing@123")
        register.click_register()

        success_msg = page.locator("//div[contains(text(),'Registeration is successful.')]")
        assert success_msg.is_visible(), "Registration success message not visible"

    def test_first_name_required(self, browser_page: Page):
        page = browser_page
        register = RegisterPage(page)

        register.open()
        register.enter_username("testuser8899")
        register.enter_first_name("")        # First name empty
        register.enter_last_name("S")
        register.enter_password("Testing@123")
        register.enter_confirm_password("Testing@123")
        register.click_register()

        error = page.locator("//label[text()='First Name']//following::div[contains(text(),'First Name is required')]")
        assert error.is_visible(), "First Name required message NOT visible"

    def test_last_name_required(self, browser_page: Page):
        page = browser_page
        register = RegisterPage(page)

        register.open()
        register.enter_username("testuser9900")
        register.enter_first_name("Shamika")
        register.enter_last_name("")         # Last name empty
        register.enter_password("Testing@123")
        register.enter_confirm_password("Testing@123")
        register.click_register()

        error = page.locator("//label[text()='Last Name']//following::div[contains(text(),'Last Name is required')]")
        assert error.is_visible(), "Last Name required message NOT visible"

    def test_password_mismatch(self, browser_page: Page):
        page = browser_page
        register = RegisterPage(page)

        register.open()
        register.enter_username("user5566")
        register.enter_first_name("Shamika")
        register.enter_last_name("S")
        register.enter_password("Testing@123")
        register.enter_confirm_password("WrongPass")
        register.click_register()

        mismatch_error = page.locator("//div[contains(text(),'Passwords do not match')]")
        assert mismatch_error.is_visible(), "Password mismatch message NOT visible"

    def test_invalid_password_policy(self, browser_page: Page):
        page = browser_page
        register = RegisterPage(page)

        register.open()
        register.enter_username("user7788")
        register.enter_first_name("Shamika")
        register.enter_last_name("S")
        register.enter_password("123")                # Invalid password
        register.enter_confirm_password("123")
        register.click_register()

        policy_error = page.locator("//div[contains(text(),'InvalidPasswordException')]")
        assert policy_error.is_visible(), "Password policy validation NOT visible"

    def test_no_success_message_without_clicking_register(self, browser_page: Page):
        page = browser_page
        register = RegisterPage(page)

        register.open()
        register.enter_username("user1111")
        register.enter_first_name("Shamika")
        register.enter_last_name("S")
        register.enter_password("Testing@123")
        register.enter_confirm_password("Testing@123")

        # DO NOT CLICK REGISTER BUTTON

        success_msg = page.locator("//div[contains(text(),'Registeration is successful.')]")

        assert not success_msg.is_visible(), "Success message visible WITHOUT clicking Register (BUG)"
