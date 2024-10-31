from selenium import webdriver
driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.maximize_window()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get("https://practice.automationtesting.in/")
x="annatester@gmail.com"
y="IamAnnaTester1234567"
my_account=driver.find_element_by_id("menu-item-50")
my_account.click()
email_reg=driver.find_element_by_id("reg_email")
email_reg.send_keys(x)
passwoord_reg=driver.find_element_by_id("reg_password")
passwoord_reg.send_keys(y)
register=driver.find_element_by_css_selector('.register> :nth-child(4) [name="register"]')
register.click()
driver.quit()


