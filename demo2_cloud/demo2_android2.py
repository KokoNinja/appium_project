












    self.driver=webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",desired_capabilities=des_cap)
    driver.implicitly_wait(30)
    yield


class TestAndroidCloud:
    def test_inavlid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        print(self.driver.page_source)
