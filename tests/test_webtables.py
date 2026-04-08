from pages.tables_page import Webtables
import time

def test_tables(browser):
    page_tables = Webtables(browser)

    page_tables.visit()
    assert not page_tables.no_data.exist()

    while page_tables.button_delete_row.exist():
        page_tables.button_delete_row.click()

    time.sleep(2)
    assert page_tables.no_data.exist()
