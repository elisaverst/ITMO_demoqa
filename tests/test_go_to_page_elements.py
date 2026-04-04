from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage
import time

def test_go_to_page_elements(browser):

    demo_qa_pages = DemoQA(browser)
    elements_page = ElementsPage(browser)

    demo_qa_pages.visit()
    time.sleep(3)

    assert demo_qa_pages.equal_url()

    demo_qa_pages.button_elements.click()
    time.sleep(3)

    assert elements_page.equal_url()
