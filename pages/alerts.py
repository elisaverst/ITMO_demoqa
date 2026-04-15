from pages.base_page import BasePage
from components.components import WebElement

class Alerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.alert_button = WebElement(driver, '//*[@id="alertButton"]')
        self.confirm_button = WebElement(driver, '//*[@id="confirmButton"]')
        self.confirm_result = WebElement(driver, '//*[@id="confirmResult"]')
        self.prompt_button = WebElement(driver, '//*[@id="promptButton"]')
        self.prompt_result = WebElement(driver, '//*[@id="promptResult"]')

        self.timer_button = WebElement(driver, '//*[@id="timerAlertButton"]')
        self.timer_result = WebElement(driver, '//*[@id="timerAlertResult"]')
