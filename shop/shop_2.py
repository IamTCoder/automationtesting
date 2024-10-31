import time
from selenium import webdriver
driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.maximize_window()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
x="annatester@gmail.com"
y="IamAnnaTester1234567"
my_account=driver.find_element_by_id("menu-item-50").click()
email_log=driver.find_element_by_id("username")
email_log.send_keys(x)
password_log=driver.find_element_by_id("password")
password_log.send_keys(y)
login=driver.find_element_by_css_selector('.login>:nth-child(3) [name="login"]').click()
shop=driver.find_element_by_id("menu-item-40").click()
html_category=driver.find_element_by_css_selector("#woocommerce_product_categories-2>.product-categories>.cat-item-19>a").click()
time.sleep(3)
quantity=driver.find_elements(By.CSS_SELECTOR, "#content>:nth-child(3) li")
assert len(quantity) == 3, f"Expected 3 products, but found {len(quantity)}"
driver.quit()
