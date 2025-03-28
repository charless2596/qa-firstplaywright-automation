from playwright.async_api import Page

def navigationContact (page: Page, firstname,lastname,email,option1,message) :
    page.goto("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"nav-contact\"]")
    page.type("[data-test=\"first-name\"]","John")
    page.type("[data-test=\"last-name\"]","Doe")
    page.type("[data-test=\"email\"]","johndoe@testing.com")
    page.wait_for_selector("[data-test=\"subject\"]")
    page.select_option("[data-test=\"subject\"]", value="Payments")
    page.type("[data-test=\"message\"]","testing message to testing testing testinng testing testing ")
    page.click("[data-test=\"contact-submit\"]")
    alert_element = page.locator('div[role="alert"].alert.alert-success')
    expected_text = "Thanks for your message! We will contact you shortly."
    actual_text = alert_element.inner_text()
    assert actual_text == expected_text

def uploadingAttachments (page: Page, firstname,lastname,email,option1,message,fileUpload) :
    page.goto("https://practicesoftwaretesting.com/")
    page.click("[data-test=\"nav-contact\"]")
    page.type("[data-test=\"first-name\"]","John")
    page.type("[data-test=\"last-name\"]","Doe")
    page.type("[data-test=\"email\"]","johndoe@testing.com")
    page.wait_for_selector("[data-test=\"subject\"]")
    page.select_option("[data-test=\"subject\"]", value="Payments")
    page.type("[data-test=\"message\"]","testing message to testing testing testinng testing testing ")
    page.set_input_files('input[type="file"]', 'myTestPlaywright/Images/sampletext.txt')
    page.locator("[data-test=\"contact-submit\"]").click()
    alert_element = page.locator('div[role="alert"].alert.alert-success')
    expected_text = "Thanks for your message! We will contact you shortly."
    actual_text = alert_element.inner_text()
    assert actual_text == expected_text