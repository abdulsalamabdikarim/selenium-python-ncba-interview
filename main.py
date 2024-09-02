from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(executable_path = "./chromedriver")
driver = webdriver.Chrome(service = service)

driver.get("https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue%26pli%3D1&ec=GAlAwAE&hl=en&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S-1019797056%3A1725133534064740&ddm=0")
# create_account_button = driver.find_element(By.LINK_TEXT, "Create account")

# create_account_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSeVfPpkd-LgbsSe-OWXEXe-dgl2HfksBjEclKxP2dLQeN7BqKGqeeR0mzbTrZEUcJ7pUA")
create_account_button = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button")

create_account_button.click()

personal_use_option = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]")
personal_use_option.click()



time.sleep(10)

driver.quit()