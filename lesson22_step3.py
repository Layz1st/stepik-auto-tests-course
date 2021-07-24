from selenium import webdriver
import time
import math

def calc(x):
  return str(int(x)+int(y))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//span[@id="num1"]')
    x = x_element.text
    print("x=: ", x)
    y_element = browser.find_element_by_xpath('//span[@id="num2"]')
    y = y_element.text
    print("y=: ", y)

    z = calc(x)
    print(z)

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)

    button = browser.find_element_by_css_selector("button.btn").click()


    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


