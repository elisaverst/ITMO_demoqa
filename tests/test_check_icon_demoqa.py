from pages.demoqa import DemoQA
import time

def test_check_icon(browser):

    demo_qa_pages = DemoQA(browser)
    demo_qa_pages.visit()
    time.sleep(3)

    demo_qa_pages.click_on_the_icon()
    time.sleep(3)

    assert demo_qa_pages.equal_url()
    assert demo_qa_pages.exist_icon()
