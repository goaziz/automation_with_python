from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

def search_automation(search_text):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('https://google.com')
    print(driver.title)
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys(search_text)
    search_bar.send_keys(Keys.RETURN)
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.save_screenshot('screenshots/image-%s.png' % now)
    time.sleep(5)
    driver.close()

search_text = str(input('Search Google or type a URL: '))
print(search_automation(search_text))
