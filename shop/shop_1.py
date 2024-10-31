import time
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
shop=driver.find_element_by_id("menu-item-40")
shop.click()
scroll=driver.execute_script("window.scrollBy(0, 300);")
html_book=driver.find_element_by_css_selector("#content>:nth-child(4) [title='Mastering HTML5 Forms'] ")
html_book.click()
#book_header=wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#content .summary.entry-summary>h1'), "HTML5 Forms"
book_header=driver.find_element(By.CSS_SELECTOR, '#content .summary.entry-summary>h1')
header_text=book_header.text
assert header_text=="HTML5 Forms"

driver.quit()





