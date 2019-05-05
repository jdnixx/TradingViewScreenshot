"""
tvchartbot.py - Tradingview scraper module

Uses Selenium to open a headless Chrome window, look up a ticker, and return a screenshot of its chart.

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


print('STARTING')


USER = "groupmebot"
PASS = "groupmebot1"


url = "https://www.tradingview.com/chart/UzJ9PCY8/#"


class TradingViewScraper:
    def __init__(self):
        print("TradingViewScraper IS INIT'ing")
        ### OPENING A HEADLESS BROWSER ###
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"--window-size=800,600")
        chrome_options.add_argument("--hide-scrollbars")
        # self.driver = webdriver.Chrome("/Program Files/chromedriver", options=chrome_options)
        chrome_options.binary_location = '/app/.apt/usr/bin/google-chrome'
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.driver.get(url)

        ### LOGGING IN ###

        # finds "log in" hyperlink (if currently on error page)
        login = self.driver.find_element_by_class_name('js-login-link')
        print("Login:")
        print(login)
        login.click()

        # wait for js login prompt
        username = WebDriverWait(self.driver, 1, 0.05).until(
            EC.presence_of_element_located((By.NAME, 'username')))
        print("Username:")
        print(username)

        # find password
        password = self.driver.find_element_by_name('password')  # if username box is found, then password is visible too


        # put in da details
        username.send_keys(USER)
        password.send_keys(PASS)
        password.send_keys(Keys.RETURN)
        print("Login info entered")


    def get_chart_screenshot_binary(self, sym):
        ### ENTERING TICKER ###

        # symbol input box (top-left)
        tickerinput = WebDriverWait(self.driver, 10, 0.05).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'input-3lfOzLDc-')))
        print("tickerinput:")
        print(tickerinput)

        tickerinput.click()
        tickerinput.send_keys(sym)

        # drop-down of matching symbols
        # tickeritem = WebDriverWait(self.driver, 10, 0.05).until(
        #     EC.presence_of_element_located((By.XPATH, '//tr[@data-item-ticker="BINANCE:BTCUSDT"]')))
        # print(tickeritem.get_attribute('data-item-ticker'))

        ### SCREENSHOT ###
        self.driver.save_screenshot('screen_shot.png')
        print("Screenshot saved")
        screenshot_binary = self.driver.get_screenshot_as_png()
        # self.driver.close()
        return screenshot_binary


tv = None
try:
    tv = TradingViewScraper()
except Exception:
    print("creating tv object failed")

bindata = tv.get_chart_screenshot_binary("ltcusd")