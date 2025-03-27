import pytest
from playwright.sync_api import sync_playwright
from fixtures.contactnavigation import navigationContact, uploadingAttachments


firstname = "John"
lastname = "Doe"
email = "johndoe@testing.com"
option1 = "Payments"
message = "testing message to testing testing testinng testing testing"
fileUpload1= "venv/Images/sampletext.txt"


@pytest.fixture(scope="function")
def setup_browser():
   
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_navigatecontact (setup_browser) :
    
    page = setup_browser 

    navigationContact(page,firstname,lastname,email,option1,message)

def test_uploadingAttachments (setup_browser) :
    
    page = setup_browser

    uploadingAttachments (page, firstname, lastname, email, option1, message, fileUpload1)