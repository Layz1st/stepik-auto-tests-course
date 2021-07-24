from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    first_window = browser.window_handles[0]

    button = browser.find_element_by_css_selector("button.btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    first = browser.find_element_by_xpath('//input[@class="form-control"][@required]').send_keys(y)
    button = browser.find_element_by_css_selector("button.btn").click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()
