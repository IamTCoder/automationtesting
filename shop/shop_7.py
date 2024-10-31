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
shop = driver.find_element(By.ID, "menu-item-40").click()
driver.execute_script("window.scrollBy(0, 450);")
html_web_app_dev = driver.find_element(By.CSS_SELECTOR, '.post-182 [data-product_id="182"]').click()
cart = driver.find_element(By.CSS_SELECTOR, "#wpmenucartli [title='View your shopping cart']").click()
proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart_totals .wc-proceed-to-checkout > a"))).click()
first_name=wait.until( EC.element_to_be_clickable((By.ID, "billing_first_name")) )
first_name.send_keys("Anna")
last_name=driver.find_element(By.ID,"billing_last_name")
last_name.send_keys("Tester")
email = driver.find_element(By.ID, "billing_email")
email.send_keys("annatester@gmail.com")
phone = driver.find_element(By.ID, "billing_phone")
phone.send_keys("8787726374")
driver.execute_script("window.scrollBy(0, 250);")
country_selector = wait.until(EC.element_to_be_clickable((By.ID, "s2id_billing_country")))
country_selector.click()
# Ввод названия страны в поле ввода и выбор варианта из выпадающего списка
country_input = wait.until(EC.visibility_of_element_located((By.ID, "s2id_autogen1_search")))
country_input.send_keys("Iceland")
# Ожидание и выбор "Iceland" из выпадающего списка
country_choice = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Iceland']")))
country_choice.click()

address = driver.find_element(By.ID, "billing_address_1")
address.send_keys("Novaya street")
post_code = driver.find_element(By.ID, "billing_postcode")
post_code.send_keys("91214")
town_city = driver.find_element(By.ID, "billing_city")
town_city.send_keys("Towm")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_pay=driver.find_element(By.CSS_SELECTOR, '#payment [value="cheque"]').click()
place_order=driver.find_element(By.CSS_SELECTOR, '#payment [value="Place order"]').click()
time.sleep(3)
thank_you = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_method=wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table.order_details >tfoot>:nth-child(3)"), "Check Payments"))
driver.quit()











