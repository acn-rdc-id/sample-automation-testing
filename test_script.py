import re
from playwright.sync_api import Playwright, sync_playwright, expect

def buy_policy_now_button():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://allianz-stg.hackydoodle.com/login")

        page.get_by_role("textbox", name="User ID").click()
        page.get_by_role("textbox", name="User ID").fill("winnielove@gmail.com")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("12345678")

        #page.wait_for_selector("text=Buy Now", timeout=10000)
        # page.click("text=Buy Now")
        # expect(page).to_have_url("https://allianz-stg.hackydoodle.com/policy-purchase")


        # Optional: wait for next page to load
        #page.wait_for_load_state("networkidle")

        browser.close()

# # Test Editable Text Assertion
# def test_user_id_field_editable():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False, slow_mo=500)
#         context = browser.new_context()
#         page = context.new_page()
#
#         page.goto("https://allianz-stg.hackydoodle.com/login")
#         #page.locator("div").filter(has_text=re.compile(r"^User ID$")).first.click()
#         page.get_by_role("textbox", name="User ID").click()
#         page.get_by_role("textbox", name="User ID").fill("winnielove@gmail.com")
#         page.get_by_role("textbox", name="Password").click()
#         page.get_by_role("textbox", name="Password").fill("12345678")
#         expect(page.get_by_role("textbox", name="User ID")).to_be_editable()
#
#         page.get_by_role("button", name="LOG IN").click()
#
#         #expect(page.get_by_role("textbox", name="Password")).to_be_editable()
#
# def test_password_field_editable():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False, slow_mo=500)
#         context = browser.new_context()
#         page = context.new_page()
#
#         page.goto("https://allianz-stg.hackydoodle.com/login")
#         #page.locator("div").filter(has_text=re.compile(r"^User ID$")).first.click()
#         page.get_by_role("textbox", name="User ID").click()
#         page.get_by_role("textbox", name="User ID").fill("winnielove@gmail.com")
#         page.get_by_role("textbox", name="Password").click()
#         page.get_by_role("textbox", name="Password").fill("12345678")
#         #expect(page.get_by_role("textbox", name="User ID")).to_be_editable()
#         expect(page.get_by_role("textbox", name="Password")).to_be_editable()
#
#         page.get_by_role("button", name="LOG IN").click()



# def buy_policy_now_button():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False, slow_mo=500)
#         page = browser.new_page()
#
#         page.goto("https://allianz-stg.hackydoodle.com/login")
#         page.wait_for_selector("text=Buy Now")  # Change selector if needed
#         page.click("text=Buy Now")

# def buy_policy_now_button():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False, slow_mo=500)
#         page = browser.new_page()
#
#         # Go to the login page
#         page.goto("https://allianz-stg.hackydoodle.com/login")
#
#         page.get_by_role("textbox", name="User ID").click()
#         page.get_by_role("textbox", name="User ID").fill("winnielove@gmail.com")
#         page.get_by_role("textbox", name="Password").click()
#         page.get_by_role("textbox", name="Password").fill("12345678")
#
#         # Wait for and click the "Buy Now" button
#         page.wait_for_selector("text=Buy Now")
#         page.click("text=Buy Now")



   # page.get_by_text("Buy now", exact=True).click()


    #expect(page.get_by_role("textbox", name="Password")).to_be_editable()

