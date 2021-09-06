from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/huge_form.html")

try:
    elems = driver.find_elements(By.TAG_NAME, 'input')
    print(len(elems))
    for i in range(len(elems)):
        elems[i].send_keys('123')
    driver.find_element(By.CLASS_NAME,'btn-default').click()
finally:
    time.sleep(3)
    driver.quit()