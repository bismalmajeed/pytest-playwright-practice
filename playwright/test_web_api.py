# Run file:      pytest playwright/test_web_api.py -v -s
# Run headed:    pytest playwright/test_web_api.py -v -s --headed
# Run one test:  pytest playwright/test_web_api.py::test_e2e_web_api -v -s

from playwright.sync_api import Playwright, expect

from utils.credentials import default_user
from utils.apiBase import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()



    #create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)
    #login
    page.goto("https://rahulshettyacademy.com/client")
    user = default_user()
    page.get_by_placeholder("email@example.com").fill(user["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(user["userPassword"])
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()

    #orders History page-> order is present.
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
