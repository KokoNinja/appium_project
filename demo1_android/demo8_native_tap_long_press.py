import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.nativekey import AndroidKey


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            # "appPackage": "org.khandacademy.android",
            "app": r"C:\Components\khan-academy-7-3-2.apk",
            # "udid": "emulator-5556"
        }

        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAdvanceCode(AppiumConfig):
    def test_tap_using_coordinates(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

            self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

            action=TouchAction(self.driver)
            action.tap(x=900,y=900,count=5)

            time.sleep(5)

    def test_lonng_press_coordinates(self):
            time.sleep(10)

    def test_long_press_webelements(self):
            time.sleep(5)
            self.driver.press_keycode(AndroidKey.HOME)
            time.sleep(2)
            self.driver.swipe(902,1174,902,794,1000)
            action=TouchAction(self.driver)
            action.long_press(self.driver.find_element(AppiumBy.))
    

