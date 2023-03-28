import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "app": "bs://67777985352261ac6114393ece93b29a761a9054",
            "platformVersion": "15",
            "deviceName": "iPhone 13 Pro",
            "bstack:options": {
                "userName": "konikanegi_4hX5RP",
                "accessKey": "YvRitqyW7EuQV2gupZCX",
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test"
            }

        }

        self.driver=webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)


class TestSampleApp(AppiumConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField[@value='Username']").send_keys("test")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@value='Password']").send_keys("test123")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-LOGIN']").send_keys("test123").click()
        actual_error=self.driver.find_element(AppiumBy.XPATH,"//XCUIElementTypeStaticText[contains(@name,'not match')]").text
        assert_that(actual_error).contains("Username and password do not match")