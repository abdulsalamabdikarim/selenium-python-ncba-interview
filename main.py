from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


# service = Service(executable_path = "/chromedriver")
driver = webdriver.Chrome()

driver.get("https://react.dev/learn/tutorial-tic-tac-toe")
time.sleep(10)

driver.quit()