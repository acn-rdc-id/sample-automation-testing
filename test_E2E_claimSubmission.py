import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://allianz-stg.hackydoodle.com/login")
    page.get_by_role("textbox", name="User ID").click()
    page.get_by_role("textbox", name="User ID").fill("testing123@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("12345678")
    page.get_by_role("button", name="LOG IN").click()
    page.get_by_text("Claims Submission").click()
    page.get_by_role("button", name="SUBMIT A CLAIM").click()
    page.get_by_role("combobox", name="Policy Number").locator("div").first.click()
    page.get_by_text("POL1748482335407").click()
    page.get_by_role("combobox", name="Type of Claim").locator("div").first.click()
    page.get_by_text("Critical Illness Claim").click()
    page.get_by_role("button", name="Next").click()
    page.locator("nx-file-uploader").filter(has_text="Diagnosis Report Add File").get_by_label("Add Driver Documents").click()
    page.locator("nx-file-uploader").filter(has_text="Diagnosis Report Add File").get_by_label("Add Driver Documents").set_input_files("Diagnosis Report.txt")
    page.locator("nx-file-uploader").filter(has_text="Medical Reports Add File").get_by_label("Add Driver Documents").click()
    page.locator("nx-file-uploader").filter(has_text="Medical Reports Add File").get_by_label("Add Driver Documents").set_input_files("Medical Reports.txt")
    page.locator("nx-file-uploader").filter(has_text="ID Proof Add File").get_by_label("Add Driver Documents").click()
    page.locator("nx-file-uploader").filter(has_text="ID Proof Add File").get_by_label("Add Driver Documents").set_input_files("ID Proof.txt")
    page.locator("nx-file-uploader").filter(has_text="Policy Document Add File").get_by_label("Add Driver Documents").click()
    page.locator("nx-file-uploader").filter(has_text="Policy Document Add File").get_by_label("Add Driver Documents").set_input_files("Policy Document.txt")
    page.get_by_role("button", name="Submit Claim").click()
    page.get_by_role("button", name="Return to Dashboard").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
