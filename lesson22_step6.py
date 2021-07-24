from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    first = browser.find_element_by_xpath('//input[@class="form-control"][@required]').send_keys(y)

    second = browser.find_element_by_xpath('//input[@class="form-check-input"][@id="robotCheckbox"][@required]').click()

    third = browser.find_element_by_xpath('//input[@class="form-check-input"][@value="robots"]').click()

    button = browser.find_element_by_css_selector("button.btn").click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()




finally:
    time.sleep(5)
    browser.quit()
