from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, poll_frequency=1)

url  = "https://suninjuly.github.io/explicit_wait2.html"

try:
    #Открываем страницу
    driver.get(url)

    #Находим Элементы страницы
    cost = (By.ID, "price")
    book_button = (By.ID, "book")

    #Дожидаемся цены в 100$ и кликаем на кнопку 
    wait.until(EC.text_to_be_present_in_element(cost, "100"))
    driver.find_element(*book_button).click()

    #Находим новые элементы на странице
    x_text = driver.find_element(By.ID, "input_value").text
    input_field = driver.find_element(By.ID, "answer")
    submit_button = driver.find_element(By.ID, "solve")

    #Находим формулу
    formula_text = driver.find_element(By.CSS_SELECTOR, "label .nowrap").text[8:26]
    print(formula_text)
    formula = formula_text.replace("ln", "math.log").replace("sin", "math.sin").replace("x", x_text)
    result = eval(formula, {"math": math})
    print(result)

    #Вставляем ответ в поле ввода и нажимаем кнопку
    input_field.send_keys(result)
    submit_button.click()
    time.sleep(10)

    #Переключаемся на алер и принимаем его
    allert = driver.switch_to.alert
    allert.accept()
    

finally:
    time.sleep(3)
    driver.quit()