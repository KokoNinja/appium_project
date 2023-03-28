import time

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


        self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)


class TestSampleApp(AppiumConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField[@value='Username']").send_keys("test")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@value='Password']").send_keys("test123")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-LOGIN']").send_keys("test123").click()
        actual_error=self.driver.find_element(AppiumBy.XPATH,"//XCUIElementTypeStaticText[contains(@name,'not match')]").text
        assert_that(actual_error).contains("Username and password do not match")

    def test_add_to_cart(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()

# add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()

        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()

    def test_add_to_cart_method2(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()

        # add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()

        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()
        # swipe and click on checkout
        print(len(self.driver.find_elements(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']")))
        print(self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed())

        size_dic = self.driver.get_window_size()
        x1 = size_dic['width'] * (50 / 100)
        y1 = size_dic['height'] * (75 / 100)

        x2 = size_dic['width'] * (50 / 100)
        y2 = size_dic['height'] * (25 / 100)

        while not self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed():
            self.driver.swipe(x1, y1, x2, y2, 1000)

        self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()

    def test_add_to_cart_mobile_command_method3(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()

        # add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()

        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()

        # # swipe and click on checkout
        # print(len(self.driver.find_elements(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']")))
        # print(self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed())
        #
        # # swipe based on visiblity
        # while not self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed():
        #     self.driver.execute_script("mobile: scroll", {"direction": "down"})

        para_dic={"direction":"down","predicateString":"name=='test-checkout'","toVisible":"True"}
        self.driver.execute_script("mobile:scroll",para_dic)

        self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()