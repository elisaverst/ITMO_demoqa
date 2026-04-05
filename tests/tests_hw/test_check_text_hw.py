from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage
import time

def test_check_footer(browser):

    demo_qa_pages = DemoQA(browser)

    demo_qa_pages.visit()
    time.sleep(3)

    assert demo_qa_pages.footer.get_text() == '© 2013-2026 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_check_text(browser):
    demo_qa_pages = DemoQA(browser)
    elements_page = ElementsPage(browser)

    demo_qa_pages.visit()
    demo_qa_pages.button_elements.click()
    time.sleep(3)

    assert elements_page.equal_url()
    assert elements_page.text.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()

    assert elements_page.icon.exist()
    assert elements_page.button_sidebar_first.exist()
    assert elements_page.button_sidebar_first_textbox.exist()
