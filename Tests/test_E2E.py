from selenium.webdriver.common.by import By
from PageObjects.homePage import homePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setUp")
class TestEndToEnd(BaseClass):

    def test_checkout(self):
        log = self.getLog()

        #HomePage variable created
        Homepage = homePage(self.driver)    #call instance driver from homePage and assign to  variable
        checkout_page = Homepage.shop_items() #Created an object within homePage, which is given for Next Page Connection


        #CheckoutPage variable Creted
        #CHECKOUT_PAGE = checkoutPage(self.driver)  #call instance driver from CheckoutPage and assign to variable

        Cards = checkout_page.getCardlist()  # I got the product List
        for product in Cards:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == 'Blackberry':
                product.find_element(By.XPATH, "div/button").click()

            log.info(productName)
            log.info(product)


        Cart_Nav_Button = checkout_page.getCartButton()
        Cart_Nav_Button.click()


        purchase_page = checkout_page.getCart_Checkout()

        #PurchasePage Variables created
        #PURCHASE_PAGE = purchasePage(self.driver)
        CountryNameBox = purchase_page.sendCountryInfo()
        CountryNameBox.send_keys("Ind")

        self.locatorPresence("India")

        CountryName = purchase_page.getCountryName()
        CountryName.click()

        CheckBox = purchase_page.Purchase_CheckBox()
        CheckBox.click()

        PurchaseButton = purchase_page.Purchase_Button()
        PurchaseButton.click()

        SuccessMessage = purchase_page.Purchase_Message()
        successMsg = SuccessMessage.text
        assert "Success! Thank you!" in successMsg
        log.info(successMsg)