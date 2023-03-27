import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

"""READ SMS FROM PHONE"""

class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "appPackage":"org.khandacademy.android"
            #"app": r"C:\Components\khan-academy-7-3-2.apk",
            #"udid": "emulator-5556"
        }

        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestArts(AppiumConfig):
    def test_list_sms(self):
        time.sleep(5)
        message = self.driver.execute_script("mobile: listSms", {"max": 2})
        print(message)
        print(message["items"])
        print(message["total"])
        print(message["items"][1])
        print(message["items"])
        print(message["items"][1]["body"])
