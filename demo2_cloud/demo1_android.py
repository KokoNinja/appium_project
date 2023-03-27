from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "app": "bs://a7edff5ce079bede689f0e24a643f1b3aad734b2",
    "platformVersion":"9.0",
    "deviceName": "Google Pixel 3",
    'bstack:options': {
        "projectName": "First Python project",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack first_test",
        # Set your access credentials
        "userName": "ninjacodepython_Pd6CmX",
        "accessKey": "87ZvNgqWNhuHzKzkbSee"
    }

}
driver=webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()
print(driver.page_source)

driver.quit()