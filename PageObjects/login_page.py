from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from PageLocators.login_page_locs import LoginPageLocs as loc


class LoginPage:
    # 属性 - 元素定位

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login(self, user, passwd):
        self.wait.until(EC.visibility_of_element_located(loc.login_button_loc))
        self.driver.find_element(*loc.username_loc).send_keys(user)
        self.driver.find_element(*loc.passwd_loc).send_keys(passwd)
        self.driver.find_element(*loc.login_button_loc).click()

    def get_error_msg_from_login_area(self):
        """
        获取登陆失败时，在登陆区域的提示。
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(loc.error_tips_from_login_area))
        return self.driver.find_element(*loc.error_tips_from_login_area).text
