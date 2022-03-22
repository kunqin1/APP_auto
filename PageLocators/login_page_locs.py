from appium.webdriver.common.mobileby import MobileBy


class LoginPageLocs:
    # 用户名输入框
    username_loc = (MobileBy.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_loc = (MobileBy.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button_loc = (MobileBy.TAG_NAME, 'button')
    # 登陆区域的提示框
    error_tips_from_login_area = (MobileBy.XPATH, '//div[@class="form-error-info"]')
    test = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(“街道的完整地址”)')
