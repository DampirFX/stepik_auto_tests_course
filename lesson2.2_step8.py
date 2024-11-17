from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.XPATH, '//input[contains(@placeholder,"first")]').send_keys("Ivan")
    browser.find_element(By.XPATH, '//input[contains(@placeholder,"last")]').send_keys("Petrov")
    browser.find_element(By.XPATH, '//input[contains(@placeholder,"email")]').send_keys("Petrov@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)
    button = browser.find_element(By.XPATH, '//button[contains(text(),"Submit")]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()