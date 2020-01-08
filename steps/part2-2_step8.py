from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    text_field1 = browser.find_element_by_name("firstname")
    text_field1.send_keys("Имя")
    text_field2 = browser.find_element_by_name("lastname")
    text_field2.send_keys("Фамилия")
    text_field3 = browser.find_element_by_name("email")
    text_field3.send_keys("Почта")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    check_box = browser.find_element_by_id("file")
    check_box.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    """# находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text"""

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()