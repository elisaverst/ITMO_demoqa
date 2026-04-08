from pages.base_page import BasePage
from components.components import WebElement

class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '//*[@id="firstName"]')
        self.last_name = WebElement(driver, '//*[@id="lastName"]')
        self.user_email = WebElement(driver, '//*[@id="userEmail"]')
        self.gender_radio_m = WebElement(driver, '//*[@id="gender-radio-1"]')
        self.gender_radio_f = WebElement(driver, '//*[@id="gender-radio-2"]')
        self.gender_radio_o = WebElement(driver, '//*[@id="gender-radio-3"]')
        self.user_number = WebElement(driver, '//*[@id="userNumber"]')
        self.button_submit = WebElement(driver, '//*[@id="submit"]')
        self.modal_dialog = WebElement(driver, '/html/body/div[3]/div/div')
        self.button_close_modal = WebElement(driver, '//*[@id="closeLargeModal"]')

        self.hobbies = WebElement(driver, '//*[@id="hobbies-checkbox-1"]')
        self.current_address = WebElement(driver, '//*[@id="currentAddress"]')
        self.user_form = WebElement(driver, '//*[@id="userForm"]')

        self.button_state = WebElement(driver, '//*[@id="state"]/div')
        self.button_NCR = WebElement(driver, '//*[contains(text(), "NCR")]')
