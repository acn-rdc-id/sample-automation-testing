*** Settings ***
Library SeleniumLibrary
Suite Setup Open Browser To Login Page
Suite Teardown Close Browser

*** Variable ***
${BROWSER} chrome
${URL} https://allianz-stg.hackydoodle.com/login
${USERNAME}
${PASSWORD}
${HOME_URL}

*** Test Case ***
Verify Login Page Loads
    Title Should Be Login - Example Staging