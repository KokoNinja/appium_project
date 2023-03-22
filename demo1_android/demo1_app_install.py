from appium import webdriver

from appium.webdriver.common.appiumby import AppiumBy


des_cap = {
    "platformName": "android",
    "deviceName": "samsung",
    "app": r"C:\Components\khan-academy-7-3-2.apk",
    "udid" : "emulator-5554"
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
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='There was an issue signing in']").text
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='First name']").send_keys("konika")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Last name']").send_keys("negi")
##DOB
# driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='First name']").send_keys("konika")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Email address']").send_keys("negikonika1@gmail.com")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Password']").send_keys("test123")


#Sign Up with correct email

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign up with email']").click()


print(driver.page_source)
