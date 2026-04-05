from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.button_menu = WebElement(driver, '/html/body/div/div/div/div/div[1]/div/div/div[3]/div/ul/li')
        self.icon = WebElement(driver, '//*[@id="root"]/header/a/img')