from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text
    z = int(x) + int(y)


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))

    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()