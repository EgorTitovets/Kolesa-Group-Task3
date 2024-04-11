#проверка последнего кода от сервера при переходе в категории

from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumwire import webdriver as wiredriver

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

        # Получаем все запросы, сделанные браузером
        requests = driver.requests

        # Находим последний статус код ответа сервера
        last_status_code = None
        for request in requests:
            if request.response:
                last_status_code = request.response.status_code
        # Выводим статус код для текущей категории
        if last_status_code is not None:
            print(f"Категория '{category}': Код ответа сервера {last_status_code}")
        else:
            print(f"Категория '{category}': Запросы не были отправлены или не было ответов от сервера")


finally:
    driver.quit()


