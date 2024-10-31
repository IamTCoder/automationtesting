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
shop=driver.find_element(By.ID,"menu-item-40").click()
driver.execute_script("window.scrollBy(0, 450);")
html_web_app_dev=driver.find_element(By.CSS_SELECTOR, '.post-182 >[data-product_id="182"]').click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 500);")
js_data_structures_and_algorithm=driver.find_element(By.CSS_SELECTOR, '.post-180 >[data-product_id="180"]').click()
cart=driver.find_element(By.CSS_SELECTOR, "#wpmenucartli> [title='View your shopping cart']").click()
delite_html=driver.find_element(By.CSS_SELECTOR, '.cart_item> .product-remove [data-product_id="182"]').click()
time.sleep(3)
undo=driver.find_element(By.CSS_SELECTOR,".woocommerce-message> a ").click()
js_quantity= (driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1) .quantity>input"))
js_quantity.clear()
js_quantity.send_keys("3")
update_basket=driver.find_element(By.NAME, "update_cart").click()
js_quantity= driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1) .quantity>input")
js_assert=js_quantity.get_attribute("value")
assert js_assert=="3"

time.sleep(3)
coupon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.coupon input[type="submit"]')))
coupon.click()

error_message=driver.find_element(By.CSS_SELECTOR, ".page-content.entry-content .woocommerce-error")
error_message_text=error_message.text
assert error_message_text=="Please enter a coupon code."

driver.quit()




