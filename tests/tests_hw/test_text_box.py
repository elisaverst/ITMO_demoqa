from pages.text_box_page import TextBox
import time

def test_clear(browser):
    text_box = TextBox(browser)
    text_box.visit()

    text_box.name.send_keys('Matthew Wilson')
    text_box.current_address.send_keys('Lincoln Road 420')
    time.sleep(2)

    text_box.submit.click_force()

    assert not text_box.name.get_dom_attribute('Full Name') == 'Matthew Wilson'
    assert not text_box.name.get_dom_attribute('Current Address') == 'Lincoln Road 420'
