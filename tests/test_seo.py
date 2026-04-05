from pages.demoqa import DemoQA

def test_check_title_deno(browser):
    demo_qa_page = DemoQA(browser)

    demo_qa_page.visit()

    assert browser.title == 'demosite'