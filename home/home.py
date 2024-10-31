from selenium import webdriver
driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.maximize_window()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
ruby=driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0  h3").click()
driver.execute_script("window.scrollBy(0, 200);")
reviews=driver.find_element_by_css_selector('#content  a[href="#tab-reviews"]').click()
driver.execute_script("window.scrollBy(0, 250);")
five_stars=driver.find_element_by_css_selector('#commentform a[class="star-5"]').click()
my_review=driver.find_element_by_id("comment")
my_review.send_keys("Nice book!")
name=driver.find_element_by_id("author")
name.send_keys("Anna")
email=driver.find_element_by_id("email")
email.send_keys("annatester@gmail.com")
submit=driver.find_element_by_id("submit").click()
driver.quit()
