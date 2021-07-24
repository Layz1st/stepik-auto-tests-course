from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_tag_name('img')
    x_number = x_element.get_attribute("valuex")
    print("x=: ", x_number)
    x = x_number
    y = calc(x)

    first = browser.find_element_by_xpath('//input[@id="answer"][@required]').send_keys(y)

    second = browser.find_element_by_xpath('//input[@class="check-input"][@id="robotCheckbox"][@required]').click()

    third = browser.find_element_by_xpath('//input[@class="check-input"][@value="robots"]').click()


    button = browser.find_element_by_css_selector("button.btn").click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


