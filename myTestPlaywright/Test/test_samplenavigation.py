from playwright.sync_api import sync_playwright
import pytest
from myTestPlaywright.fixtures import samplenavig

@pytest.fixture(scope="function")
def setup_browser():
   
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_Homenagivation (setup_browser) :
    
    page = setup_browser

    samplenavig.homenavigation(page)


def test_HandToolsnavigation (setup_browser) :

    page = setup_browser

    samplenavig.handtoolsnavigation(page)
    

def test_powerToolsnavigation (setup_browser) :

    page = setup_browser

    samplenavig.powertoolsnavigation(page)

def test_otherToolsnavigaation (setup_browser) :
    
    page = setup_browser

    samplenavig.othertoolsnavigaation(page)

def test_RentalToolsnavigation (setup_browser) :

    page = setup_browser

    samplenavig.rentaltoolsnavigation(page)
    

def test_navigateLanguage (setup_browser) :
    
    page = setup_browser

    samplenavig.navigateLanguage(page)
