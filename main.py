from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


service = Service(executable_path = "./chromedriver")
driver = webdriver.Chrome(service = service)

driver.get("https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue%26pli%3D1&ec=GAlAwAE&hl=en&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S-1019797056%3A1725133534064740&ddm=0")

time.sleep(10)

driver.quit()