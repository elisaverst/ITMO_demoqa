from pages.demoqa import DemoQA
import time

def test_check_icon(browser):

    demo_qa_pages = DemoQA(browser)

    demo_qa_pages.visit()
    time.sleep(3)

    demo_qa_pages.icon.click()
    time.sleep(3)

    assert demo_qa_pages.equal_url()
    assert demo_qa_pages.icon.exist()
