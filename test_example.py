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

        browser.close()

# Auto Script for E2E testing
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://allianz-stg.hackydoodle.com/login")
#     page.locator("div").filter(has_text=re.compile(r"^User ID$")).first.click()
#     page.get_by_role("textbox", name="User ID").fill("winnielove@gmail.com")
#
#     expect(page.get_by_role("textbox", name="User ID")).to_be_editable()
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("12345678")
#     page.get_by_role("button", name="LOG IN").click()
#     page.get_by_text("Buy now", exact=True).click()
#     page.get_by_role("combobox", name="I am a").locator("div").first.click()
#     page.get_by_role("option", name="Male", exact=True).locator("div").first.click()
#     page.get_by_role("button", name="Open calendar").click()
#     page.get_by_role("button", name="June 6,").click()
#     page.get_by_role("button", name="Next").click()
#     page.locator("#plan-2-label div").click()
#     page.get_by_role("button", name="Next").click()
#     page.get_by_role("combobox", name="Title *").locator("div").first.click()
#     page.get_by_role("option", name="Mr", exact=True).locator("div").first.click()
#     page.get_by_role("textbox", name="Name as per NRIC *").click()
#     page.get_by_role("textbox", name="Name as per NRIC *").fill("Test ")
#     page.get_by_role("combobox", name="Nationality / Citizenship *").locator("div").first.click()
#     page.get_by_role("option", name="Malaysian").locator("div").first.click()
#     page.get_by_role("textbox", name="NRIC No. *").click()
#     page.get_by_role("textbox", name="NRIC No. *").fill("070606121234")
#     page.get_by_role("combobox", name="Country of Birth *").locator("div").first.click()
#     page.locator(".cdk-overlay-backdrop").click()
#     page.get_by_role("textbox", name="NRIC No. *").click()
#     page.get_by_role("textbox", name="NRIC No. *").press("ArrowRight")
#     page.get_by_role("textbox", name="NRIC No. *").fill("070606-12-1235")
#     page.get_by_role("combobox", name="Country of Birth *").locator("div").first.click()
#     page.get_by_role("option", name="Malaysia").locator("div").first.click()
#     page.get_by_role("combobox", name="Country Code *").locator("div").first.click()
#     page.get_by_role("option", name="60").locator("div").first.click()
#     page.get_by_role("textbox", name="Mobile Number *").click()
#     page.get_by_role("textbox", name="Mobile Number *").fill("12345678")
#     page.get_by_role("textbox", name="Email *").click()
#     page.get_by_role("textbox", name="Email *").fill("testing123@gmail.com")
#     page.get_by_role("combobox", name="Occupation *").locator("div").first.click()
#     page.get_by_role("option", name="Administrators").locator("div").first.click()
#     page.get_by_role("combobox", name="Purpose of Transaction *").locator("div").first.click()
#     page.get_by_text("Education").click()
#     page.get_by_role("button", name="Next").click()
#     page.locator("#nx-checkbox-1-label span").click()
#     page.locator("#nx-checkbox-2-label span").click()
#     page.locator("#nx-checkbox-3-label span").click()
#     page.locator("#nx-checkbox-0-label span").click()
#     page.get_by_role("button", name="Submit").click()
#     page.get_by_role("button", name="Success").click()
#     page.get_by_role("button", name="Go to Details").click()
#
#
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)


# import re
# from playwright.sync_api import Playwright, sync_playwright, expect
#
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://allianz-stg.hackydoodle.com/login")
#
#     #Expect the text box User ID to be empty
#     expect(page.get_by_role("textbox", name="User ID")).to_be_empty();
#     page.get_by_role("textbox", name="User ID").click()
#     page.get_by_role("textbox", name="User ID").fill("winnielove@gmail.com")
#
#     #Expect the text box Password to be empty
#     expect(page.get_by_role("textbox", name="Password")).to_be_empty();
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("12345678")
#
#     #Login button
#     page.get_by_role("button", name="LOG IN").click()
#
#     #Click "Buy Now" button
#     page.get_by_text("Buy now", exact=True).click()
#
#     #Choose gender and yob
#     page.get_by_role("combobox", name="I am a").locator("div").first.click()
#     page.get_by_role("option", name="Male", exact=True).locator("div").first.click()
#     page.get_by_role("button", name="Open calendar").click()
#     page.get_by_role("button", name="June 1,").click()
#     page.get_by_role("button", name="Next").click()
#
#     #User click medium plan
#     page.locator("#plan-2-label div").click()
#     expect(page.get_by_role("cell", name="Plan 300k")).to_be_visible()
#     expect(page.get_by_role("cell", name="Monthly", exact=True)).to_be_visible()
#     expect(page.get_by_role("cell", name="RM 150 / monthly")).to_be_visible()
#
#     #User click high plan
#     page.locator("#plan-3-label div").click()
#     expect(page.get_by_role("cell", name="Plan 500k")).to_be_visible()
#     expect(page.get_by_role("cell", name="Monthly", exact=True)).to_be_visible()
#     expect(page.get_by_role("cell", name="RM 250 / monthly")).to_be_visible()
#     page.get_by_role("button", name="Next").click()
#
#     # page.get_by_role("combobox", name="Title *").locator("div").first.click()
#     # page.get_by_role("option", name="Mr", exact=True).locator("div").first.click()
#     # page.get_by_role("textbox", name="Name as per NRIC *").click()
#     # page.get_by_role("textbox", name="Name as per NRIC *").fill("Winnie")
#     # page.get_by_role("combobox", name="Nationality / Citizenship *").locator("div").first.click()
#     # page.get_by_role("option", name="Malaysian").locator("div").first.click()
#     # page.get_by_role("textbox", name="NRIC No. *").click()
#     # page.get_by_role("textbox", name="NRIC No. *").fill("070601-14-5213")
#     # page.get_by_role("combobox", name="Country of Birth *").locator("div").first.click()
#     # page.get_by_role("option", name="Malaysia").locator("div").first.click()
#     # page.get_by_role("combobox", name="Country Code *").locator("div").first.click()
#     # page.get_by_role("option", name="60").locator("div").first.click()
#     # page.get_by_role("textbox", name="Mobile Number *").click()
#     # page.get_by_role("textbox", name="Mobile Number *").fill("1234567890")
#     # page.get_by_role("textbox", name="Email *").click()
#     # page.get_by_role("textbox", name="Email *").fill("winnielove@gmail.com")
#     # page.get_by_role("combobox", name="Occupation *").locator("div").first.click()
#     # page.get_by_role("option", name="Babysitter").locator("div").first.click()
#     # page.get_by_role("combobox", name="Purpose of Transaction *").locator("div").first.click()
#     # page.get_by_role("option", name="Protection, Savings,").locator("div").first.click()
#     # page.get_by_role("button", name="Next").click()
#     #
#     # #Confirmation page
#     # page.locator("#nx-checkbox-1-label span").click()
#     # page.locator("#nx-checkbox-2-label span").click()
#     # page.locator("#nx-checkbox-3-label span").click()
#     # page.locator("#nx-checkbox-0-label span").click()
#     # page.get_by_role("button", name="Submit").click()
#     # page.get_by_role("button", name="Success").click()
#
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)

