from pages.modal_dialogs_page import ModalDialogsPage
import  time

def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.button_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    browser.refresh()
    time.sleep(2)

    modal_dialogs_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.forward()

    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'demosite'

    browser.set_window_size(1000, 1000)
