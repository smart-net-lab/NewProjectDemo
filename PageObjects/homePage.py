from selenium.webdriver.common.by import By

from PageObjects.checkoutPage import checkoutPage


class homePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.XPATH, "//input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.CSS_SELECTOR, "input[type='password']")
    gen = (By.ID, "exampleFormControlSelect1")
    allRadioButtons = (By.XPATH, "//label[contains(text(),'Student')]")
    bDay = (By.CSS_SELECTOR, "input[name='bday']")
    submit = (By.CSS_SELECTOR, ".btn.btn-success")
    alertSuccess = (By.CSS_SELECTOR, ".alert-success")


    def shop_items(self):
        self.driver.find_element(*homePage.shop).click()
        checkout_page = checkoutPage(self.driver)
        return checkout_page

    def get_name(self):
        return self.driver.find_element(*homePage.name)

    def get_email(self):
        return self.driver.find_element(*homePage.email)

    def get_pwd(self):
        return self.driver.find_element(*homePage.password)

    def get_gender(self):
        return self.driver.find_element(*homePage.gen)

    def get_radio(self):
        return self.driver.find_element(*homePage.allRadioButtons).click()

    def get_birthday(self):
        return self.driver.find_element(*homePage.bDay)

    def submit_button(self):
        return self.driver.find_element(*homePage.submit).click()

    def alert_msg(self):
        return self.driver.find_element(*homePage.alertSuccess)





