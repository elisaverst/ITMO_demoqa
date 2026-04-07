from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, '//*[@id="userName"]')
        self.current_address = WebElement(driver, '//*[@id="currentAddress"]')
        self.submit = WebElement(driver, '//*[@id="submit"]')
        self.output_name = WebElement(driver, '//*[@id="name"]')
        self.output_current_address = WebElement(driver, '//*[@id="name"]')
