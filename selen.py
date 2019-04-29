from selenium import webdriver
# from PIL import Image
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.tradingview.com/chart/HW3jYB1J/"

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

height=480

#Open another headless browser with height extracted above
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument(f"--window-size=640,{height}")
chrome_options.add_argument("--hide-scrollbars")
driver = webdriver.Chrome("/app/.apt/usr/bin/google-chrome", options=chrome_options)

driver.get(url)
#pause 3 second to let page loads
# time.sleep(3)
#save screenshot
driver.save_screenshot('screen_shot.png')
# driver.close()