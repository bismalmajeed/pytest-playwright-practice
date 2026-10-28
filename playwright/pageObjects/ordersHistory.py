from playwright.sync_api import TimeoutError

from .orderDetails import OrderDetailsPage


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self, orderId):
        row = self.page.locator("tr").filter(has_text=orderId)
        # new orders can take a moment to show up in the list, so reload and retry
        for _ in range(3):
            try:
                row.first.wait_for(timeout=7000)
                break
            except TimeoutError:
                self.page.reload()
        row.get_by_role("button", name="View").click()
        ordersDetailsPage = OrderDetailsPage(self.page)
        return ordersDetailsPage
