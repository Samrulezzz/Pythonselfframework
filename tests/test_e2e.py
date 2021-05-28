from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        checkOutpage = homePage.shopItems()
        log.info("getting all the Card titles")
        cards = checkOutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            # print(cardText)
        if cardText == "Blackberry":
            checkOutpage.getCardFooter()[i].click()

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkOutpage.cardbutton().click()

        confirmPage = checkOutpage.checkOutItems()
        log.info("Entering country name as ind")
        # CheckOutPage.checkOutItems().click()
        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        # self.driver.find_element_by_id("country").send_keys("ind")
        confirmPage.confirmcountry().send_keys("ind")
        # time.sleep(5)

        self.verifyLinkPresence("India")

        # self.driver.find_element_by_link_text("India").click()
        confirmPage.selcountey().click()
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        confirmPage.checkoutbx().click()

        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("Text recived from application is"+textMatch)
        assert ("Success! Thank s you!" in textMatch)