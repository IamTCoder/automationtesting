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
wait = WebDriverWait(driver, 20)
x="annatester@gmail.com"
y="IamAnnaTester1234567"
my_account=driver.find_element(By.ID,"menu-item-50").click()
email_log=driver.find_element(By.ID,"username")
email_log.send_keys(x)
password_log=driver.find_element(By.ID, "password")
password_log.send_keys(y)
login=driver.find_element(By.NAME, "login").click()
shop=driver.find_element(By.ID,"menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
android_book=driver.find_element(By.CSS_SELECTOR,".post-169>a").click()
high_price=driver.find_element(By.CSS_SELECTOR, ".price>del>span")
high_price_check=high_price.text
assert "600.00" in high_price_check
low_price=driver.find_element(By.CSS_SELECTOR, ".price>ins>span")
low_price_check=low_price.text
assert "450.00" in low_price_check
picture=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".images>a")))
picture.click()
picture_close=wait.until(EC. element_to_be_clickable((By.CSS_SELECTOR, ".pp_fade .pp_close")))
picture_close.click()
driver.quit()


