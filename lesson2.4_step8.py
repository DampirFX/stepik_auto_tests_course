from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin
import time


def calc(x):
    y = log(abs(12 * sin(x)))
    return y
try:
    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element(By.ID, "book")
    button.click()
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(y))
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()