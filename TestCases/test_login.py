
"""
前置
测试数据：18684720553  python

"""
import pytest
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage

from TestDatas import login_datas as td


@pytest.mark.usefixtures("open_app")
class TestLogin:

    # 逆向场景 - 登陆失败 - 数据格式无效
    @pytest.mark.parametrize("case", td.invalid_data)
    def test_login_failed_invalid_data(self, case, open_app):
        LoginPage(open_app).login(case["user"], case["passwd"])
        assert LoginPage(open_app).get_error_msg_from_login_area() == case["check"]

    # 正向场景 - 登陆成功
    def test_login_success(self, open_app):
        LoginPage(open_app).login(*td.valid_user)
        assert HomePage(open_app).is_exit_exist()

    # def test_login_success(self):
    #     # 登陆页面 - 登陆 - 18684720553 python
    #     # 断点：首页 - 获取退出元素是否存在
    #     pass
