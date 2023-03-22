from appium import webdriver

des_cap = {
    "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
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
driver=webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()
