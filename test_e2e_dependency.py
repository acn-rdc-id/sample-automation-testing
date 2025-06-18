import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://allianz-stg.hackydoodle.com/login")
    page.get_by_role("textbox", name="User ID").click()
    page.get_by_role("textbox", name="User ID").fill("winnielove@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("12345678")
    page.get_by_role("button", name="LOG IN").click()
    page.get_by_text("Allianz Life Policies").click()
    page.get_by_text("POL1749199845778").click()
    page.get_by_role("button", name="Insured Info").click()
    page.get_by_role("button", name="Beneficiary More information").click()
    page.get_by_role("button", name="Add Beneficiary").click()
    page.get_by_placeholder("e.g. John Doe").click()
    page.get_by_placeholder("e.g. John Doe").fill("Ashlyn")
    page.get_by_role("combobox").locator("div").first.click()
    page.get_by_role("option", name="Parent").locator("div").first.click()
    page.locator("#nx-input-12").click()
    page.locator("#nx-input-12").fill("40")
    page.get_by_role("button", name="Add Beneficiary").click()
    page.get_by_placeholder("e.g. John Doe").click()
    page.get_by_placeholder("e.g. John Doe").fill("Helena")
    page.locator("tr:nth-child(2) > td:nth-child(2) > .nx-formfield--type-nx-dropdown > .nx-formfield__wrapper > .nx-formfield__row > .nx-formfield__flexfield > .nx-formfield__input-container > .nx-formfield__input > .nx-dropdown > .nx-dropdown__container").click()
    page.get_by_role("option", name="Sibling").locator("div").first.click()
    page.locator("#nx-input-14").click()
    page.locator("#nx-input-14").fill("60")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("row", name="Ashlyn").get_by_role("button").click()
    page.get_by_role("row", name="Helena").get_by_role("button").click()
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
