from TestData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest

class TestHomePage(BaseClass):

    def test_formsubmission(self,getData):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        log.info("first name is"+getData["firstname"] )
        homepage.getName().send_keys(getData["firstname"])
        homepage.getemail().send_keys(getData["lastname"])
        homepage.getChcekBox().click()

        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.getsubmitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success " in alertText)

        self.driver.refresh()  #
    @pytest.fixture(params = HomePageData.HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param
