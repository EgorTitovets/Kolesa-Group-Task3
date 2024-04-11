#проверка статус кода URL

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Функция для проверки кода ответа сервера
def check_response_code(url):
    response = requests.get(url)
    return response.status_code == 200

try:
    driver = webdriver.Chrome()
    driver.get("https://avtoelon.uz")

    # Нахождение и открытие раздела "Машины"
    cars_link = driver.find_element(By.XPATH, "//a[@class='menu-link selected' and @id='currentSection' and @href='/avto/']")
    cars_link.click()

    # Список категорий
    categories = ["Легковые", "Мототехника", "Водный транспорт"]

    # Переход в каждую категорию и проверка кода ответа сервера
    for category in categories:
        category_link = driver.find_element(By.XPATH, f"//span[@class='action-link' and @title='{category}']")
        category_link.click()

        # Получение URL текущей страницы
        current_url = driver.current_url

        # Проверка кода ответа сервера
        if check_response_code(current_url):
            print(f"Категория '{category}': Код ответа сервера 200 (OK)")
        else:
            print(f"Категория '{category}': Ошибка - Код ответа сервера не 200")

finally:
    driver.quit()
