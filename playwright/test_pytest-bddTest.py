# Run file:      pytest playwright/test_pytest-bddTest.py -v -s
# Run headed:    pytest playwright/test_pytest-bddTest.py -v -s --headed
# Run one test:  pytest playwright/test_pytest-bddTest.py::test_name -v -s

import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils
from utils.credentials import default_user


def resolve(username, password):
    # feature file holds placeholders; real values come from data/credentials.json
    if username == "default_user":
        user = default_user()
        return user["userEmail"], user["userPassword"]
    return username, password


scenarios('features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    username, password = resolve(username, password)
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    shared_data['order_id'] = orderId


@given('the user is on landing page')
def user_on_landing_page(browserInstance, shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    shared_data['login_page'] = loginPage


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    username, password = resolve(username, password)
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboard_page'] = dashboardPage


@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data['dashboard_page']
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    shared_data['orderHistory_page'] = orderHistoryPage


@when('select the orderId')
def select_order_id(shared_data):
    orderHistoryPage = shared_data['orderHistory_page']
    orderId = shared_data['order_id']
    ordersDetailsPage = orderHistoryPage.selectOrder(orderId)
    shared_data['orderDetails_page'] = ordersDetailsPage


@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    ordersDetailsPage = shared_data['orderDetails_page']
    ordersDetailsPage.verifyOrderMessage()
