from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value")
    y = calc(int(x.text))
    text_field = browser.find_element_by_id("answer")
    text_field.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()