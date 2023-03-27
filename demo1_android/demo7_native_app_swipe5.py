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
            # "appPackage": "org.khandacademy.android",
            "app": r"C:\Components\khan-academy-7-3-2.apk",
            # "udid": "emulator-5556"
        }

        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestArts(AppiumConfig):

    def test_the_himalayas_topics(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        # id is resource-id only
        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        # ACCESSIBILITY_ID is content-desc in android
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Search tab").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']").click()

        # swipe until //android.widget.TextView[@text='Art oF Asia'] presence
        while len(self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Art oF Asia']")) == 0:
            self.driver.swipe(902, 1174, 924, 794, 1000)  # not going tow ork with latest appium server
        time.sleep(5)

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Art oF Asia']").click()

        size_dic = self.driver.get_window_size()
        print(size_dic)
        x1 = size_dic['width'] * (50 / 100)
        y1 = size_dic['height'] * (75 / 100)

        x2 = size_dic['width'] * (50 / 100)
        y2 = size_dic['height'] * (25 / 100)

        # swipe until //android.widget.TextView[@text='Art oF Asia'] presence
        while len(self.driver.find_elements(AppiumBy.XPATH, "//*[@text='Art oF Asia']")) == 0:
            self.driver.swipe(x1, y1, x2, y2, 1000)


