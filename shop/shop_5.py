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
driver.execute_script("window.scrollBy(0, 400);")
html_web_app_dev=driver.find_element(By.CSS_SELECTOR, '.post-182 >[data-product_id="182"]').click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 400);")
item_quantity=wait.until(EC. visibility_of_element_located((By.CSS_SELECTOR, "#wpmenucartli >a> .cartcontents")))
item_quantity_text=item_quantity.text
print(item_quantity)
assert "1 Item" in item_quantity_text, f"Expected '1 Item', but got {item_quantity_text}"
item_price=driver.find_element(By.CSS_SELECTOR, "#wpmenucartli .amount")
item_price_text=item_price.text
assert "₹180.00" in item_price_text, f"Expected '₹180.00', but got {item_price_text}"
cart=driver.find_element(By.CSS_SELECTOR, "#wpmenucartli> [title='View your shopping cart']").click()
subtotal=wait.until(EC. visibility_of_element_located((By.CSS_SELECTOR, '#page-34 .cart-subtotal [data-title="Subtotal"] > span ')))
total=wait.until(EC. visibility_of_element_located((By.CSS_SELECTOR, '#page-34 .order-total strong>span ')))

driver.quit()

