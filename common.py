from selenium.webdriver.support. wait import WebDriverWait 
from selenium webdriver support import expected_conditions as ec

class CommonOps:
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_eleent_located(locator))
    
    def find(self, lcoator):
        return self.driver.find_element(*locator)