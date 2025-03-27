from playwright.sync_api import Page


def sortingnameAZ (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_selector("[data-test=\"sort\"]")
    page.select_option("[data-test=\"sort\"]", value="name,asc")

def sortingnameZA (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_selector("[data-test=\"sort\"]")
    page.select_option("[data-test=\"sort\"]", value="name,desc")

def sortingnameHL (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_selector("[data-test=\"sort\"]")
    page.select_option("[data-test=\"sort\"]", value="price,desc")

def sortingnameLH (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_selector("[data-test=\"sort\"]")
    page.select_option("[data-test=\"sort\"]", value="price,asc")

def sortingbysearch (page: Page) :
    page.goto("https://practicesoftwaretesting.com/")
    page.type("[data-test=\"search-query\"]","Pliers")
    page.click("[data-test=\"search-submit\"]")

def sortingbyslider (page: Page, slider_handle,target_value, slider_width, new_position, new_value) :

    page.goto("https://practicesoftwaretesting.com/")

    slider_handle = page.wait_for_selector("span.ngx-slider-pointer")

    slider_handle.click()

    target_value = 150 
    slider_width = 200
    new_position = (target_value / 200) * slider_width

    slider_handle.hover()
    page.mouse.move(slider_handle.bounding_box()['x'] + new_position, slider_handle.bounding_box()['y'])
    page.mouse.down()
    page.mouse.move(slider_handle.bounding_box()['x'] + new_position, slider_handle.bounding_box()['y'], steps=10)
    page.mouse.up()

    new_value = slider_handle.get_attribute("aria-valuenow")


