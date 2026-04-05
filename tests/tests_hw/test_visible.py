from pages.accordian_page import AccordianPage
import time

def test_visible_accordion(browser):
    accordion_page = AccordianPage(browser)

    accordion_page.visit()

    assert accordion_page.text_lorem.visible()

    accordion_page.what_is_lorem.click()
    time.sleep(2)
    assert not accordion_page.text_lorem.visible()

def test_visible_accordion_default(browser):
    accordion_page = AccordianPage(browser)

    accordion_page.visit()
    assert not accordion_page.text_where_does_1.visible()
    assert not accordion_page.text_where_does_2.visible()
    assert not accordion_page.text_why_do.visible()
