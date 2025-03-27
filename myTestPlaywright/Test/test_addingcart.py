import pytest
from playwright.sync_api import sync_playwright
from fixtures.addingcart import cartadded,addingcartwithmultiplequantity


Product_Name1 = "product-01JPWKGAS994T3FG7Q1HHM1TGH"
Product_Name2 = "product-01JPWKGASBDVPDFCW45VK8GGEG"
Product_Name3 = "product-01JPWKGASDB4AZ0CGKPRBK7QEM"
Product_Category = "category-01JQ6FBQP3FRSMKBVV7HYCPG0S"
Product_Selected = "[data-test=\"product-01JQ6FBQQVKMF9KGFJFAXTG3V4\"]"

@pytest.fixture(scope="function")
def setup_browser():
   
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_cartadded (setup_browser) :
    
    page = setup_browser

    cartadded(page,Product_Name1,Product_Name2,Product_Name3)


def test_addingcartwithmultiplequantity (setup_browser) :
    
    page = setup_browser
    
    addingcartwithmultiplequantity(page,Product_Category, Product_Selected)

