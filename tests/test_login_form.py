from pages.form_page import FormPage
import time

def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()

    time.sleep(2)

    form_page.first_name.send_keys('John')
    form_page.last_name.send_keys('Doe')
    form_page.user_email.send_keys('jdoe@example.com')
    form_page.gender_radio_m.click()
    form_page.user_number.send_keys('9876543210')
    time.sleep(2)

    form_page.button_submit.click()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
