from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/registration2.html")

try:
    elems = driver.find_elements_by_xpath("//div[@class='first_block']//input")
    for i in range(len(elems)):
        elems[i].send_keys('123asd')
    driver.find_element_by_class_name('btn-default').click()

finally:
    time.sleep(3)
    driver.close()