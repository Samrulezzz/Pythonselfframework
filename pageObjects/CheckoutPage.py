from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    cardTitle = (By.CSS_SELECTOR,".card-title a")
    cardFooter = (By.CSS_SELECTOR,".card-footer button")
    cardbtn = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    # self.driver.find_element_by_css_selector((".card-footer button"))
    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def cardbutton(self):
        return self.driver.find_element(*CheckOutPage.cardbtn)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

