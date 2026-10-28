# Run file:      pytest playwright/test_Network1.py -v -s
# Run headed:    pytest playwright/test_Network1.py -v -s --headed
# Run one test:  pytest playwright/test_Network1.py::test_Network_1 -v -s

import pytest
from playwright.sync_api import Page, Playwright, expect
from utils.credentials import default_user
from utils.apiBase import APIUtils

fakePayloadOrderResponse = {"data": [], "message": "No Orders"}


#-> api call from browser-> api call contact server return back response to browser-> browser use response to generate html
def intercept_response(route):
    route.fulfill(
        json=fakePayloadOrderResponse
    )


@pytest.mark.smoke
def test_Network_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    user = default_user()
    page.get_by_placeholder("email@example.com").fill(user["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(user["userPassword"])
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
