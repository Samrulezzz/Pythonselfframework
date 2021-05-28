from selenium.webdriver.common.by import By


class ConfirmPage:
    selCountry = (By.ID, "country")
    # self.driver.find_element_by_link_text("India").click()\
    country = (By.LINK_TEXT, "India")

    checkout = (By.XPATH,"//div[@class='checkbox checkbox-primary']")

    def __init__(self, driver):
        self.driver = driver

    def confirmcountry(self):
        return self.driver.find_element(*ConfirmPage.selCountry)

    def selcountey(self):
        return self.driver.find_element(*ConfirmPage.country)

    def checkoutbx(self):
        return self.driver.find_element(*ConfirmPage.checkout)




