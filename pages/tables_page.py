from pages.base_page import BasePage
from components.components import WebElement


class Webtables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.driver.maximize_window()

        self.button_add = WebElement(driver, '//*[@id="addNewRecordButton"]')

        self.registration_form = WebElement(driver, '/html/body/div[3]/div/div')
        self.first_name = WebElement(driver, '//*[@id="firstName"]')
        self.last_name = WebElement(driver, '//*[@id="lastName"]')
        self.email = WebElement(driver, '//*[@id="userEmail"]')
        self.age = WebElement(driver, '//*[@id="age"]')
        self.salary = WebElement(driver, '//*[@id="salary"]')
        self.department = WebElement(driver, '//*[@id="department"]')
        self.registration_submit = WebElement(driver, '//*[@id="submit"]')

        self.table_first_name = WebElement(driver, '/html/body/div/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[1]')
        self.table_last_name = WebElement(driver, '/html/body/div/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[2]')
        self.table_email = WebElement(driver, '/html/body/div/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[4]')
        self.table_age = WebElement(driver, '/html/body/div/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[3]')
        self.table_salary = WebElement(driver, '/html/body/div/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[5]')
        self.table_department = WebElement(driver, '/html/body/div/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[6]')

        self.edit_button = WebElement(driver, '//*[@id="edit-record-4"]')
        self.button_delete_row = WebElement(driver, '//*[@id="delete-record-4"]')
        self.no_data = WebElement(driver, 'div.rt-noData')