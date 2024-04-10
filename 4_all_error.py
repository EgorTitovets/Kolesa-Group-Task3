
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumwire import webdriver as wiredriver
import pyautogui

driver = wiredriver.Chrome()

try:
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

        print(f"Категория: {category}")

        # Получаем все запросы, сделанные браузером
        requests = driver.requests

        # Проверяем статусы ответов сервера
        success = True
        for request in requests:
            if request.response:
                status_code = request.response.status_code
                if status_code // 100 != 2:
                    success = False
                    print(f" Все запросы с сервера 2хх, кроме URL: {request.url}, Статус код: {status_code}")

        if success:
            print("  Код ответа с сервера: 200")
        print("==========================================")

finally:
    driver.quit()

