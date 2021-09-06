import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()

try:
    driver.get('http://suninjuly.github.io/get_attribute.html')
    x = driver.find_element_by_id('treasure').get_attribute('valuex')
    driver.find_element_by_id('answer').send_keys(calc(x))
    driver.find_element_by_id('robotCheckbox').click()
    driver.find_element_by_id('robotsRule').click()
    driver.find_element(By.CLASS_NAME, 'btn-default').click()

finally:
    time.sleep(7)
    driver.quit()