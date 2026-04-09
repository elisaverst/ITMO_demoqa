from pages.tables_page import Webtables
import time

def test_tables_add(browser):
    page_tables = Webtables(browser)

    page_tables.visit()

    assert page_tables.button_add.exist()
    time.sleep(1)

    page_tables.button_add.click()
    assert page_tables.registration_form.exist()

    page_tables.registration_submit.click()
    assert page_tables.registration_form.exist()

    page_tables.first_name.send_keys('John')
    page_tables.last_name.send_keys('Doe')
    page_tables.email.send_keys('test@example.com')
    page_tables.age.send_keys('12')
    page_tables.salary.send_keys('100')
    page_tables.department.send_keys('Department')
    page_tables.registration_submit.click()

    assert page_tables.table_first_name.get_text() == 'John'
    assert page_tables.table_last_name.get_text() == 'Doe'
    assert page_tables.table_age.get_text() == '12'
    assert page_tables.table_email.get_text() == 'test@example.com'
    assert page_tables.table_salary.get_text() == '100'
    assert page_tables.table_department.get_text() == 'Department'

    page_tables.edit_button.click()
    assert page_tables.registration_form.exist()

    page_tables.first_name.clear()
    page_tables.first_name.send_keys('James')
    page_tables.registration_submit.click()

    assert page_tables.table_first_name.get_text() == 'James'

    page_tables.button_delete_row.click()

    assert not page_tables.table_first_name.exist()
    assert not page_tables.table_last_name.exist()
    assert not page_tables.table_age.exist()
    assert not page_tables.table_email.exist()
    assert not page_tables.table_salary.exist()
    assert not page_tables.table_department.exist()
