import os

desired_caps = {
        "automationName": "UiAutomator2",  # 使用哪个自动化引擎,appium1.x可以不用写
        "platformName": "Android",  # 使用哪个移动操作系统平台
        "platformVersion": '7.1.2',  # 移动操作系统版本
        "deviceName": "emulator-5554",  # 使用的移动设备或模拟器的种类,需要在cmd命令下，敲adb devices查看
        "appPackage": "com.lemon.lemonban",  # 所要测试的app的包名，获取命令：aapt dump badging apk路径，查看package: name=
        "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
        # 所要测试app的入口页面，获取命令：aapt dump badging apk路径，查看launchable-activity: name='
        "noReset": True  # 在此会话之前，请勿重置应用程序状态
    }
# 端口号
host = 'http://127.0.0.1:4723/wd/hub'

# 通用的普通用户
user = ("18684720553", "python")
