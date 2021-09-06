from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/explicit_wait2.html')
try:
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    driver.find_element_by_id('book').click()
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,'answer')))
    driver.find_element_by_id('answer').send_keys(calc(driver.find_element_by_id('input_value').text))
    driver.find_element_by_id('solve').click()
    time.sleep(3)
    driver.switch_to.alert.accept()


finally:
    #assert

    driver.close()