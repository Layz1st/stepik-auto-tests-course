from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    first = browser.find_element_by_xpath('//input[@class="form-control"][@required]').send_keys(y)

    second = browser.find_element_by_xpath('//input[@class="form-check-input"][@id="robotCheckbox"][@required]').click()

    third = browser.find_element_by_xpath('//input[@class="form-check-input"][@value="robots"]').click()


    button = browser.find_element_by_css_selector("button.btn").click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


