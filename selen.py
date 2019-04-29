"""
Original script idea from:
https://stackoverflow.com/questions/51653344/taking-screenshot-of-whole-page-with-python-selenium-and-firefox-or-chrome-headl
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from PIL import Image
from selenium.webdriver.chrome.options import Options
import time


SYMBOL = 'btcusd'

url = "https://www.tradingview.com/chart/UzJ9PCY8/#"

#run first time to get scrollHeight
# driver = webdriver.Chrome("/Program Files/chromedriver")
# driver.get(url)
# #pause 3 second to let page load
# time.sleep(3)
# #get scroll Height
# height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
# print(height)
# #close browser
# driver.close()

height=600

#Open another headless browser with height extracted above
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument(f"--window-size=800,{height}")
chrome_options.add_argument("--hide-scrollbars")
driver = webdriver.Chrome("/Program Files/chromedriver", options=chrome_options)
# driver = webdriver.Chrome("/Program Files/chromedriver", options=chrome_options)

driver.get(url)
#pause 3 second to let page loads
# time.sleep(3)
# ----------


### LOGGING IN ###

login = driver.find_element_by_class_name('js-login-link')
print(login)
login.click()


username = WebDriverWait(driver, 1, 0.05).until(
    EC.presence_of_element_located((By.NAME, 'username')))

print(username)

password = driver.find_element_by_name('password')

username.send_keys(USER)
password.send_keys(PASS)
password.send_keys(Keys.RETURN)


### ENTERING TICKER ###

tickerinput = WebDriverWait(driver, 10, 0.05).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'input-3lfOzLDc-')))

tickerinput.send_keys(SYMBOL)

binancebtcusd = WebDriverWait(driver, 10, 0.05).until(
    EC.presence_of_element_located((By.XPATH, '//tr[@data-item-ticker="BINANCE:BTCUSDT"]')))
print(binancebtcusd.get_attribute('data-item-ticker'))








#save screenshot
driver.save_screenshot('screen_shot.png')
driver.close()