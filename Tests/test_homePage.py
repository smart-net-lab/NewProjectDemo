import pytest


from PageObjects.homePage import homePage
from TestData.HomeTestData import HomeTestData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_SignUpForm(self, getdata):
        log = self.getLog()

        HOMEPAGE = homePage(self.driver)

        log.info("Entered Name: " + getdata["firstName"])
        HOMEPAGE.get_name().send_keys(getdata["firstName"])

        log.info("Entered Email: " + getdata["email"])
        HOMEPAGE.get_email().send_keys(getdata["email"])

        HOMEPAGE.get_pwd().send_keys(getdata["passward"])

        self.selectOptionByText(HOMEPAGE.get_gender(), getdata["gender"])

        HOMEPAGE.get_radio()
        HOMEPAGE.get_birthday().send_keys('12','12','2024')
        HOMEPAGE.submit_button()
        SuccessMessage = HOMEPAGE.alert_msg()
        assert SuccessMessage == HOMEPAGE.alert_msg()

        self.driver.refresh()


    @pytest.fixture(params=HomeTestData.Home_Test_Data)
    def getdata(self, request):
        return request.param


