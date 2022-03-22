import pytest
from appium import webdriver
from TestDatas import global_datas as gd


@pytest.fixture(scope='class')
def open_app():
    desired_caps = gd.desired_caps
    driver = webdriver.Remote(gd.host, desired_caps)
    driver.implicitly_wait(10)
    yield driver

