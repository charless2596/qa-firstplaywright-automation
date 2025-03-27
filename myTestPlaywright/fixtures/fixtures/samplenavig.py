from playwright.async_api import Page

def homenavigation (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    assert page.title() == "Practice Software Testing - Toolshop - v5.0"
    page.click("[data-test=\"nav-home\"]")

def handtoolsnavigation (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"nav-categories\"]")
    page.click("[data-test=\"nav-hand-tools\"]")
    assert page.locator("h2[data-test='page-title']").get_attribute("data-test") == "page-title"

def powertoolsnavigation (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"nav-categories\"]")
    page.click("[data-test=\"nav-power-tools\"]")
    assert page.locator("h2[data-test='page-title']").get_attribute("data-test") == "page-title"

def othertoolsnavigaation (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"nav-categories\"]")
    page.click("[data-test=\"nav-other\"]")
    assert page.locator("h2[data-test='page-title']").get_attribute("data-test") == "page-title"

def rentaltoolsnavigation (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"nav-categories\"]")
    page.click("[data-test=\"nav-rentals\"]")
    assert page.locator("h1[data-test='page-title']").text_content() == "Rentals"

def navigateLanguage (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"language-select\"]")
    page.click("[data-test=\"lang-en\"]")