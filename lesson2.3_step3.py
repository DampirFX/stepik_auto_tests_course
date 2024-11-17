from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

def calc(x):
    y = log(abs(12 * sin(x)))
    return y

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(y))
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()