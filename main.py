from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_xpath("//button[@id='book']")
    button.click()

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    first = browser.find_element_by_xpath('//input[@class="form-control"][@required]').send_keys(y)
    button = browser.find_element_by_xpath('//button[@type="submit"]').click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
finally:

    time.sleep(5)
    browser.quit()