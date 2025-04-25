from selenium import webdriver
from selenium.webdriver.common.by import By

def function():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов с правильными CSS-селекторами
    user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')  # ID
    password = driver.find_element(By.CSS_SELECTOR, '#password')     # ID
    submit = driver.find_element(By.CSS_SELECTOR, '.btn_action')     # Класс ?
    # submit = driver.find_element(By.CSS_SELECTOR, 'login-button') #почему не могу использовать ID?

    if user_name and password and submit:
        print("Элементы найдены")
    else:
        print("Один или несколько элементов не найдены")


function()