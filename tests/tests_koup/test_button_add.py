from pages.koup_page import Koup
from pages.koup_add_page import KoupAdd
import time

def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add_page = KoupAdd(browser)
    koup_page.visit()
    time.sleep(3)

    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    koup_page.link_add.click()
    assert koup_add_page.equal_url()

    assert koup_add_page.button_add.get_text() == 'Add Element'

    assert koup_add_page.button_add.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        koup_add_page.button_add.click()

    assert koup_add_page.buttons_delete.check_count_elements(4)

    for element in koup_add_page.buttons_delete.find_elements():
        assert element.text == 'Delete'

    assert koup_add_page.buttons_delete.get_text() == 'Delete'

    while koup_add_page.buttons_delete.exist():
        koup_add_page.buttons_delete.click()

    assert not koup_add_page.buttons_delete.exist()
