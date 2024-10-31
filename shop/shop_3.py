import time
from selenium import webdriver
driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.maximize_window()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
x="annatester@gmail.com"
y="IamAnnaTester1234567"
my_account=driver.find_element(By.ID,"menu-item-50").click()
email_log=driver.find_element(By.ID,"username")
email_log.send_keys(x)
password_log=driver.find_element(By.ID, "password")
password_log.send_keys(y)
login=driver.find_element(By.NAME, "login").click()
shop=driver.find_element(By.ID,"menu-item-40").click()
select_default=driver.find_element(By.CSS_SELECTOR, '[name="orderby" ]> [value="menu_order"]')
default=select_default.get_attribute("selected")
assert default is not None
select_element=driver.find_element(By.NAME,"orderby")
sort=Select(select_element)
sort.select_by_visible_text("Sort by price: high to low")
select_element=driver.find_element(By.NAME,"orderby")
check_sort=driver.find_element(By.CSS_SELECTOR, '[name="orderby" ]> [value="price-desc"]')
price_desc=check_sort.get_attribute("selected")
assert default is not None

driver.quit()
