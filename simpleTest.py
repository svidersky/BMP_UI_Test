# Simple example of using Nerrvana with Python+webdriver
# Please note that we are not a Python guys, so corrections on contact@deepshiftlabs.com are appreciated )

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

# see http://www.nerrvana.com/docs/using-messages
def notify_system(msg, level):
    print 'will notify system: ' + msg
    driver.implicitly_wait(0.1)
    try:
        driver.find_element_by_id("SYS_NOTE@"+str(level)+"@"+msg)
    finally:
        driver.implicitly_wait(15)
        return True

print 'Demo Python+Webdriver+Nerrvana Test started'

driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME)
driver.implicitly_wait(2)

driver.get("http://en.wikipedia.org")

driver.find_element_by_id("searchInput").send_keys("Selenium")
driver.find_element_by_id("searchInput").submit()

notify_system("Search submitted, will wait for a second", 2);

time.sleep(1)

notify_system("Will check for text presence", 2);

if "This article is about the chemical element." in driver.find_element_by_tag_name("body").text:
    notify_system("Test passed - text presents on the page.", 3);
else:
    notify_system("Test FAILED - text does not present on the page.", 5);

notify_system("Making a screenshot...", 1);
driver.get_screenshot_as_file('./screenshot.png')
notify_system("Screenshot saved to ./screenshot.png.", 2);

notify_system("Closing browser.", 2);
driver.quit()

print 'Test finished'