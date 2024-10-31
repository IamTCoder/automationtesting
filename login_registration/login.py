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
email_log=driver.find_element_by_id("username")
email_log.send_keys(x)
passwoord_log=driver.find_element_by_id("password")
passwoord_log.send_keys(y)
login=driver.find_element_by_css_selector('.login>:nth-child(3) [name="login"]')
login.click()
logout=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-36 .woocommerce-MyAccount-navigation>ul>:nth-child(6)>a")))
driver.quit()



