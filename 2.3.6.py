import math
import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()

try:
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    #x = int(driver.find_element_by_id('input_value').text)
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    driver.switch_to.window(driver.window_handles[1])
    #driver.switch_to.alert.accept()

    driver.find_element_by_id('answer').send_keys(calc(int(driver.find_element_by_id('input_value').text)))
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()

finally:
    # print(os.path.dirname(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))
    time.sleep(7)
    driver.quit()