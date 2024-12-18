from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    elem = browser.find_element(By.TAG_NAME, "img")
    x = elem.get_attribute("valuex")
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()