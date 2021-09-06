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
    driver.get('http://suninjuly.github.io/alert_accept.html')
    #x = int(driver.find_element_by_id('input_value').text)
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    driver.switch_to.alert.accept()
    #time.sleep(1)

    # #Select(driver.find_element_by_id('dropdown')).select_by_visible_text(str(x+y))
    # driver.find_element_by_name('firstname').send_keys('123')
    # driver.find_element_by_name('lastname').send_keys('123')
    # driver.find_element_by_name('email').send_keys('123')
    # #y=os.path.join(os.path.abspath(os.path.dirname(__file__)), '1.txt')
    # #driver.find_element_by_id('file').send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), '1.txt'))
    #
    # #driver.execute_script('return arguments[0].scrollIntoView(true);', driver.find_element_by_id('robotCheckbox'))
    # #driver.find_element_by_id('robotCheckbox').click()
    # #driver.find_element_by_id('robotsRule').click()
    driver.find_element_by_id('answer').send_keys(calc(int(driver.find_element_by_id('input_value').text)))
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()

finally:
    # print(os.path.dirname(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))
    time.sleep(7)
    driver.quit()