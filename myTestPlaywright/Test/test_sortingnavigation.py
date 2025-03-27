from playwright.sync_api import sync_playwright
from fixtures import sortingnavigation
import pytest


slider_handle = "span.ngx-slider-pointer"
target_value = 150
slider_width = 200
new_position = (target_value / 200) * slider_width
new_value = "aria-valuenow"

@pytest.fixture(scope="function")
def setup_browser():
   
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_sortingnameAZ (setup_browser) :
    
    page = setup_browser

    sortingnavigation.sortingnameAZ(page)

def test_sortingnameZA (setup_browser) :
    
    page = setup_browser

    sortingnavigation.sortingnameZA(page)

def test_sortingnameHL (setup_browser) :
    
    page = setup_browser

    sortingnavigation.sortingnameHL(page)

def test_sortingnameLH (setup_browser) :
    
    page = setup_browser

    sortingnavigation.sortingnameLH(page)

def test_sortingbysearch (setup_browser) :
    
    page = setup_browser

    sortingnavigation.sortingbysearch(page)

def test_sortingbyslider (setup_browser) :

    page = setup_browser

    sortingnavigation.sortingbyslider(page, slider_handle, target_value, slider_width, new_position, new_value)
