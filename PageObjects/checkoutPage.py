from selenium.webdriver.common.by import By

from PageObjects.purchasePage import purchasePage


class checkoutPage:

    def __init__(self, driver):
        self.driver = driver

    CardTitle = (By.XPATH, "//div[@class='card h-100']")
    CardName = (By.XPATH, "div/h4/a")
    CardFooter = (By.XPATH, "div/button")

    CartButton = (By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']")
    CartCheckoutButton = (By.XPATH, "//button[@class='btn btn-success']")


#driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    def getCardlist(self):
        return self.driver.find_elements(*checkoutPage.CardTitle)

    def getCardName(self):
        return self.driver.find_element(*checkoutPage.CardName)

    def getCardFooter(self):
        return self.driver.find_element(*checkoutPage.CardFooter)

    def getCartButton(self):
        return self.driver.find_element(*checkoutPage.CartButton)

    def getCart_Checkout(self):
        self.driver.find_element(*checkoutPage.CartCheckoutButton).click()
        purchase_page = purchasePage(self.driver)
        return purchase_page

