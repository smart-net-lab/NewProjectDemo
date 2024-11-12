from selenium.webdriver.common.by import By


class purchasePage:

    def __init__(self, driver):
        self.driver = driver

    CountryInfo = (By.CSS_SELECTOR, "#country")
    CountryName = (By.LINK_TEXT, "India")
    AcknowledgeBox = (By.CSS_SELECTOR, ".checkbox-primary")
    Purchasebutton = (By.CSS_SELECTOR, ".btn-success")
    SuccessMessage = (By.CSS_SELECTOR, ".alert-success")




    def sendCountryInfo(self):
        return self.driver.find_element(*purchasePage.CountryInfo)

    def getCountryName(self):
        return self.driver.find_element(*purchasePage.CountryName)

    def Purchase_CheckBox(self):
        return self.driver.find_element(*purchasePage.AcknowledgeBox)

    def Purchase_Button(self):
        return self.driver.find_element(*purchasePage.Purchasebutton)

    def Purchase_Message(self):
        return self.driver.find_element(*purchasePage.SuccessMessage)
