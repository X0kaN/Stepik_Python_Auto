from selenium import webdriver
import time
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/find_link_text")

try:
    link=str(math.ceil(math.pow(math.pi, math.e)*10000))
    print(link)
    driver.find_element_by_link_text(link).click()
    driver.find_element_by_name("first_name").send_keys("Kirill")
    driver.find_element_by_name("last_name").send_keys("123qwe")
    driver.find_element_by_name("firstname").send_keys("City")
    driver.find_element_by_id("country").send_keys("Country")
    driver.find_element_by_class_name('btn-default').click()

finally:
    time.sleep(3)
    driver.close()