from playwright.sync_api import Playwright

from utils.credentials import default_user


class APIUtils:

    def getToken(self, playwright: Playwright):

        user = default_user()
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": user["userEmail"], "userPassword": user["userPassword"]})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        products = api_request_context.post("/api/ecom/product/get-all-products",
                                            data={},
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"})
        productId = products.json()["data"][0]["_id"]
        ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": productId}]}
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=ordersPayLoad,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"
                                                     })
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId
