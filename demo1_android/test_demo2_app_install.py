from appium import webdriver

from appium.webdriver.common.appiumby import AppiumBy


des_cap = {
    "platformName": "android",
    "deviceName": "samsung",
    "app": r"C:\Components\khan-academy-7-3-2.apk",
    "udid" : "emulator-5556"
}

driver=webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Enter an e-mail address or username']").send_keys("konikanegi@einfochips.com")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Password']").send_keys("test")
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()
actual_error=driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='There was an issue signing in']").text
print(actual_error)


print(driver.page_source)
time.sleep(5)
driver.quit()