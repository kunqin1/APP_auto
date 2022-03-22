from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver

from PageLocators.home_page_locs import HomePageLocs as loc


class HomePage:

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.wait = WebDriverWait(driver, 6)

    def is_exit_exist(self):
        """
        如果存在，则返回True,如果不存在，则返回False
        :return:
        """
        try:
            self.wait.until(EC.visibility_of_element_located(loc.exit_loc))
        except:
            return False
        else:
            return True
