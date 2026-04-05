from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text = WebElement(driver, '//*[@id="root"]/div/div/div/div[2]')
        self.icon = WebElement(driver, '//*[@id="root"]/header/a/img')
        self.button_sidebar_first = WebElement(driver, '//*[@id="root"]/div/div/div/div[1]/div/div/div[1]/span')
        self.button_sidebar_first_textbox = WebElement(driver, '//*[@id="item-0"]')
        self.button_sidebar_first_checkbox = WebElement(driver, '//*[@id="item-1"]')
        self.button_first_menu = WebElement(driver, '/html/body/div/div/div/div/div[1]/div/div/div[1]/div/ul/li')
