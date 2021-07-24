from selenium import webdriver
import time
import os
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element_by_xpath('//input[@name="firstname"][@required]').send_keys('andrew')
    second = browser.find_element_by_xpath('//input[@name="lastname"][@required]').send_keys('les')
    third = browser.find_element_by_xpath('//input[@name="email"][@required]').send_keys('g@mail.co')



    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)  # добавляем к этому пути имя файла
    element = browser.find_element_by_css_selector('[type="file"]')
    element.send_keys(file_path)
    time.sleep(1)

    button = browser.find_element_by_css_selector("button.btn").click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()







finally:
    time.sleep(5)
    browser.quit()
