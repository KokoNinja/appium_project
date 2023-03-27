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
            "app": r"C:\Components\khan-academy-7-3-2.apk",
            "udid":"emulator-5556"
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


def TestLogin(AppiumConfig):
    def test_invalid_login(self):

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().descriptionContains("email")').send_keys("dina")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().descriptionContains("pass")').send_keys("test")
        #click on sign in
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in").instance(1)').click()
        #get the text "There was an issue in signing it"
        actual_error= self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("issue")').text
        print(actual_error)
