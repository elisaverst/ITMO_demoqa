from pages.modal_dialogs_page import ModalDialogsPage
import time

def test_size(browser):
    modal_dialog_page = ModalDialogsPage(browser)

    modal_dialog_page.visit()

    assert modal_dialog_page.small_modal_button.exist()
    assert modal_dialog_page.large_modal_button.exist()

    modal_dialog_page.small_modal_button.click()
    time.sleep(2)
    assert modal_dialog_page.small_modal_button.exist()
    modal_dialog_page.small_modal_close.click()

    modal_dialog_page.large_modal_button.click()
    time.sleep(2)
    assert modal_dialog_page.large_modal_button.exist()
    modal_dialog_page.large_modal_close.click()
