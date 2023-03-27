import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\Components\com.bsl.hyundai_2021-08-09.apk"
            #"udid": "emulator-5556"
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestLocationMedia(AppiumConfig):
    def test_allow_location_media(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='SIGN UP!']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Name*']").send_keys("dina")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Mobile Number*']").send_keys(
            "99999999")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Email ID*']").send_keys("dina")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password*']").send_keys("test123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Confirm Password*']").send_keys(
            "test123")
        self.driver.find_element(AppiumBy.XPATH,
                                 "//android.widget.EditText[@text='android.widget.CheckBox']").click()
