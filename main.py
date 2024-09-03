from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service(executable_path = "./chromedriver")
driver = webdriver.Chrome(service = service)

driver.get("https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue%26pli%3D1&ec=GAlAwAE&hl=en&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S-1019797056%3A1725133534064740&ddm=0")
# create_account_button = driver.find_element(By.LINK_TEXT, "Create account")

# create_account_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSeVfPpkd-LgbsSe-OWXEXe-dgl2HfksBjEclKxP2dLQeN7BqKGqeeR0mzbTrZEUcJ7pUA")
create_account_button = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button")

create_account_button.click()

time.sleep(3)
personal_use_option = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]")
personal_use_option.click()



first_name = driver.find_element(By.XPATH, "//*[@id='firstName']")
first_name.send_keys("John")
first_name.send_keys(Keys.RETURN)

last_name = driver.find_element(By.XPATH, "//*[@id='lastName']")
last_name.send_keys("Doe")
last_name.send_keys(Keys.RETURN)
time.sleep(15)

birth_month = driver.find_element(By.XPATH, "//*[@id='month']")
birth_month.click()
january = driver.find_element(By.XPATH, "//*[@id='month']/option[2]")
january.click()
time.sleep(3)

birth_day = driver.find_element(By.XPATH, "//*[@id='day']")
birth_day.click()
birth_day.send_keys("01")
birth_day.send_keys(Keys.RETURN)
time.sleep(3)

birth_year = driver.find_element(By.XPATH, "//*[@id='year']")
birth_year.click()
birth_year.send_keys("2000")
birth_year.send_keys(Keys.RETURN)
time.sleep(3)

gender = driver.find_element(By.XPATH, "//*[@id='gender']")
gender.click()
male_option = driver.find_element(By.XPATH, "//*[@id='gender']/option[3]")
male_option.click()
time.sleep(5)

next_button = driver.find_element(By.XPATH, "//*[@id='birthdaygenderNext']/div/button/span")
next_button.click()

time.sleep(5)

email_field = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div[1]/div/div[1]/input")
email_field.click()
email_field.send_keys("rrrdddssswwwaaa")
time.sleep(3)

next_button2 = driver.find_element(By.XPATH, "//*[@id='next']/div/button/span")
next_button2.click()
time.sleep(5)

password = driver.find_element(By.XPATH, "//*[@id='passwd']/div[1]/div/div[1]/input")
# password.click()
password.send_keys("N3333331")
password.send_keys(Keys.RETURN)
time.sleep(3)

confirm_password = driver.find_element(By.XPATH, "//*[@id='confirm-passwd']/div[1]/div/div[1]/input")
# password.click()
confirm_password.send_keys("N3333331")
time.sleep(3)
next_button3 = driver.find_element(By.XPATH, "//*[@id='createpasswordNext']/div/button/span")
next_button3.click()
time.sleep(3)



driver.quit()