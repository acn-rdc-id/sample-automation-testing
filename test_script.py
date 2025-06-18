import re
from playwright.sync_api import Playwright, sync_playwright, expect

# Test Editable Text Assertion
def test_user_id_field_editable():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://allianz-stg.hackydoodle.com/login")
        #page.locator("div").filter(has_text=re.compile(r"^User ID$")).first.click()
        page.get_by_role("textbox", name="User ID").click()
        page.get_by_role("textbox", name="User ID").fill("winnielove@gmail.com")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("12345678")
        expect(page.get_by_role("textbox", name="User ID")).to_be_editable()

        page.get_by_role("button", name="LOG IN").click()

        #expect(page.get_by_role("textbox", name="Password")).to_be_editable()

def test_password_field_editable():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://allianz-stg.hackydoodle.com/login")
        #page.locator("div").filter(has_text=re.compile(r"^User ID$")).first.click()
        page.get_by_role("textbox", name="User ID").click()
        page.get_by_role("textbox", name="User ID").fill("winnielove@gmail.com")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("12345678")
        #expect(page.get_by_role("textbox", name="User ID")).to_be_editable()
        expect(page.get_by_role("textbox", name="Password")).to_be_editable()

        page.get_by_role("button", name="LOG IN").click()

        #expect(page.get_by_role("textbox", name="Password")).to_be_editable()

        #test
        browser.close()
