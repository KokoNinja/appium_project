import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    @pytest.fixture(scope='function', autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "app": "bs://a7edff5ce079bede689f0e24a643f1b3aad734b2",
            "deviceName": "Google Pixel 3",
            "platformVersion": "9.0",
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                # Set your access credentials
                "userName": "ninjacodepython_Pd6CmX",
                "accessKey": "87ZvNgqWNhuHzKzkbSee"
            }

        }

        self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",
                                       desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAndroidCloud(AppiumConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        print(self.driver.page_source)

    def test_sign_up_email_test(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH,
                                 "//android.widget.EditText[@text='Enter an e-mail address or username']").send_keys(
            "konikanegi@einfochips.com")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password']").send_keys("test")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='First name']").send_keys("konika")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Last name']").send_keys("negi")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Birthday']").send_keys()
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").clear()
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").send.keys("Aug")

        # choose 20
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").clear()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").send_keys(
            "20")

        # choose 1995
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").clear()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").send_keys(
            "1995")

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='OK']").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Email address']").send_keys(
            "negikonika1@gmail.com")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password']").send_keys("test123")
