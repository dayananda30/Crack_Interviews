from selenium import webdriver #Importing Python Client WebDriver Library
from selenium.webdriver.common.action_chains import ActionChains#Importing ActionChains for Implementing Mouse , drag and drop operations.
from selenium.common.exceptions import WebDriverException


driver = webdriver.Chrome('C:\Users\ddr\Desktop\Selenium_Drivers\chromedriver_win32\chromedriver.exe')

print('The Selenium Driver Instance is : {}'.format(driver))


driver.get('https://www.youtube.com/')
driver.implicitly_wait(10)


print("The Current URL is : {}".format(driver.current_url))

print("Driver name is : {} ".format(driver.name))

print("Windows Handle is : {}".format(driver.current_window_handle))


handles = driver.window_handles
numofWindowHandles = len(handles)
print("The list of Window Handles : {}:".format(driver.window_handles))

#If you want to switch the handle
for handle in range(numofWindowHandles):
    driver.switch_to_window(handles[handle])
    print('The Title of the Windows is : {}'.format(driver.title))

driver.implicitly_wait(20)

action =  ActionChains(driver)

# How to get x and Y coordinates
element = driver.find_element_by_xpath('//*[@id="text"]')
location = element.location
size = element.size
print(location)
print(size)


action.move_by_offset(32.0,-990.0)
action.perform()

print("Completed")





