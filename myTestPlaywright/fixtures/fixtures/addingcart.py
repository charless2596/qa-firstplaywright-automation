from playwright.async_api import Page

def cartadded (page : Page, product1, product2, product3):
    page.goto("https://practicesoftwaretesting.com/")
    page.click(".card-img-top")
    page.click("[data-test=\"add-to-cart\"]")
    page.click("[data-test=\"nav-home\"]")
    page.click(".card-img-top")
    page.click("[data-test=\"add-to-cart\"]")
    page.click("[data-test=\"nav-home\"]")
    page.click(".card-img-top")
    page.click("[data-test=\"add-to-cart\"]")


def addingcartwithmultiplequantity (page: Page, category, selectedprod):
    page.goto("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"product-01JQ6FBQQVKMF9KGFJFAXTG3V4\"]")
    page.click("img.card-img-top")
    page.click("[data-test=\"increase-quantity\"]")
    page.click("[data-test=\"increase-quantity\"]")
    page.click("[data-test=\"add-to-cart\"]")