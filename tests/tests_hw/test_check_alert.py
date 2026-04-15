from pages.alerts import Alerts
import time

def test_alerts(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.timer_button.click()
    time.sleep(10)
    assert alert_page.alert()
    assert alert_page.alert().text == 'This alert appeared after 5 seconds'
