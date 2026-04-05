from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage
import time

def test_check_icon(browser):

    demo_qa_pages = DemoQA(browser)
    elements_page = ElementsPage(browser)

    demo_qa_pages.visit()
    time.sleep(3)

    assert demo_qa_pages.footer.get_text() == '© 2013-2026 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    demo_qa_pages.button_elements.click()
    time.sleep(3)

    assert elements_page.equal_url()
    assert elements_page.text.get_text() == 'Please select an item from left to start practice.'
