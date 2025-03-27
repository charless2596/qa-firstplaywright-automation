import pytest
from playwright.sync_api import Page


def registrationInpt (page: Page,firstname,lastname,birthdate,street,postal,city,state,country,phone,email,password) :
    page.goto ("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"nav-sign-in\"]")
    page.click("[data-test=\"register-link\"]")
    page.type("[data-test=\"first-name\"]", "John")
    page.type("[data-test=\"last-name\"]", "Doe")
    page.fill("[data-test=\"dob\"]", "1994-08-21")
    page.type("[data-test=\"street\"]", "Testing new street block 3")
    page.type("[data-test=\"postal_code\"]", "1234")
    page.type("[data-test=\"city\"]", "Testing City")
    page.type("[data-test=\"state\"]", "Test")
    page.wait_for_selector("[data-test=\"country\"]")
    page.select_option("[data-test=\"country\"]", value= "PH")
    page.type("[data-test=\"phone\"]", "1234567890")
    page.type("[data-test=\"email\"]", "newtesting@gmail.com")
    page.type("[data-test=\"password\"]", "_Kellinquinn2596")
    page.click("[data-test=\"register-submit\"]")

def signup (page: Page, email, password) :
    page.goto("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"nav-sign-in\"]")
    page.type("[data-test=\"email\"]", "newtesting@gmail.com")
    page.type("[data-test=\"password\"]", "_Kellinquinn2596")
    page.click("[data-test=\"login-submit\"]")

def forgotpassw (page: Page, email) :
    page.goto("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"nav-sign-in\"]")
    page.click("[data-test=\"forgot-password-link\"]")
    page.type("[data-test=\"email\"]", "newtesting@yopmail.com")
    page.click("[data-test=\"forgot-password-submit\"]")

# def addtofavorites (page: Page,email,password,search) : 
#     page.goto("https://practicesoftwaretesting.com/")
#     page.click('[data-test="nav-sign-in"]')
#     page.type("[data-test=\"email\"]", "newtesting@gmail.com")
#     page.type("[data-test=\"password\"]", "_Kellinquinn2596")
#     page.click('[data-test="login-submit"]')
#     page.wait_for_load_state()
#     # page.click('[data-test="nav-home"]')
#     # page.type("[data-test=\"search-query\"]", "Hammer")
#     # page.click("[data-test=\"search-submit\"]")
#     # page.click("[data-test=\"product-01JPWKGASNNRWETT86PCG928XA\"]")
#     # page.click("[data-test=\"add-to-favorites\"]")