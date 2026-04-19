from pages.base_page import BasePage
from components.components import WebElement

class DemoQA(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '//*[@id="root"]/header/a')
        self.button_elements = WebElement(driver, '//*[@id="root"]/div/div/div[2]/div/a[1]/div/div')
        self.footer = WebElement(driver, '//*[@id="root"]/footer/span')

        self.h5 = WebElement(driver, 'div.card h5')
