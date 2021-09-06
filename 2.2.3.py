import math
import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()

try:
    driver.get('http://suninjuly.github.io/selects2.html')
    driver.execute_script("document.title='Script executing';alert('Robots at work');")
    x = int(driver.find_element_by_id('num1').text)

    y = int(driver.find_element_by_id('num2').text)
    print(x+y)
    Select(driver.find_element_by_id('dropdown')).select_by_visible_text(str(x+y))
    #driver.find_element_by_id('answer').send_keys(calc(x))
    #driver.find_element_by_id('robotCheckbox').click()
    #driver.find_element_by_id('robotsRule').click()
    driver.find_element(By.CLASS_NAME, 'btn-default').click()

finally:
    time.sleep(7)
    driver.quit()