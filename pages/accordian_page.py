from pages.base_page import BasePage
from components.components import WebElement

class AccordianPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.what_is_lorem = WebElement(driver, '//*[@id="accordianContainer"]/div/div[1]/h2/button')
        self.text_lorem = WebElement(driver, '//*[@id="accordianContainer"]/div/div[1]/div/div/p')
        self.text_where_does_1 = WebElement(driver, '//*[@id="accordianContainer"]/div/div[2]/div/div/p[1]')
        self.text_where_does_2 = WebElement(driver, '//*[@id="accordianContainer"]/div/div[2]/div/div/p[2]')
        self.text_why_do = WebElement(driver, '//*[@id="accordianContainer"]/div/div[3]/div/div/p')
