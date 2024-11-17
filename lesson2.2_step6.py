from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from math import log, sin


def calc(x):
    y = log(abs(12 * sin(x)))
    return y

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(int(x))

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(y))

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()