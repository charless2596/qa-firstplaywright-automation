import pytest
from playwright.sync_api import sync_playwright
from fixtures.registrationnav import registrationInpt, signup, forgotpassw

firstname = "John"
lastname = "Doe"
birthdate = "1994-08-21"
street = "Testing new street block 3"
postal = "1234"
city = "Testing City"
state = "Test"
country = "PH"
phone = "1234567890"
email = "newtesting@gmail.com"
password = "_Kellinquinn2596"
search = "Hammer"


@pytest.fixture(scope="function")
def setup_browser():
   
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_userRegistration (setup_browser) :

    page = setup_browser

    registrationInpt(page,firstname,lastname, birthdate, street, postal, city, state, country, phone, email, password)
    

def test_signUp (setup_browser) :

    page = setup_browser

    signup(page,email,password) 
    

def test_forgotPassword (setup_browser) :
    
    page = setup_browser

    forgotpassw (page,email)


# def test_favorites (setup_browser) :

#     page = setup_browser

#     addtofavorites(page,email,password,search)
    






