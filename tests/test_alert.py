from pages.alerts import Alerts
import time

def test_alerts(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.alert_button.click()
    time.sleep(2)
    assert alert_page.alert()

def test_alerts_text(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.alert_button.click()
    assert alert_page.alert().text == 'You clicked a button'

    alert_page.alert().accept()
    assert not alert_page.alert()

def test_confirm(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.confirm_button.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirm_result.get_text() == 'You selected Cancel'

def test_prompt(browser):
    alert_page = Alerts(browser)
    name = 'Lisa'

    alert_page.visit()
    alert_page.prompt_button.click()
    time.sleep(2)
    alert_page.alert().send_keys(name)
    alert_page.alert().accept()
    assert alert_page.prompt_result.get_text() == f'You entered {name}'
