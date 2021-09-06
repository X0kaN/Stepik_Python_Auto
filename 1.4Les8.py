from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/find_xpath_form")

try:
    driver.find_element_by_name("first_name").send_keys("Kirill")
    driver.find_element_by_name("last_name").send_keys("123qwe")
    driver.find_element_by_name("firstname").send_keys("City")
    driver.find_element_by_id("country").send_keys("Country")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)
finally:
    driver.close()