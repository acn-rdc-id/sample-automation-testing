import re
from playwright.sync_api import Playwright, sync_playwright, expect

def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://allianz-stg.hackydoodle.com/login")

        test_user_id_field_editable(page)

        page.get_by_role("button", name="LOG IN").click()

        context.close()
        browser.close()


    # Test Editable Text Assertion
def test_user_id_field_editable():
    page.get_by_role("textbox", name="User ID").click()
    page.get_by_role("textbox", name="User ID").fill("winnielove@gmail.com")
    expect(page.get_by_role("textbox", name="User ID")).to_be_editable()

# def test_password_field_editable():
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("12345678")
#     expect(page.get_by_role("textbox", name="Password")).to_be_editable()
#


