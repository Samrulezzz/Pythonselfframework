from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    def __init__(self, driver):
        self.driver = driver

    name = (By.CSS_SELECTOR, "[name='name']")

    email = (By.NAME, "email")
    checkbx = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submitF = (By.XPATH, "//input[@value='Submit']")
    success = (By.CSS_SELECTOR, "[class*='alert-success']")



    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutpage = CheckOutPage(self.driver)
        return checkOutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getChcekBox(self):
        return self.driver.find_element(*HomePage.checkbx)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getsubmitForm(self):
        return self.driver.find_element(*HomePage.submitF)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.success)
