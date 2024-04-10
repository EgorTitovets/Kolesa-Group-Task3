from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

try:
    link = "https://avtoelon.uz"
    browser = webdriver.Chrome()
    browser.get(link)

    section_cars = browser.find_element(By.XPATH, "//a[@class ='menu-link selected' and @ id='currentSection' and text()='Машины']")
    section_cars.click()


    current_url = browser.current_url
    print("Раздел Машины")
    response_status_code = requests.get(current_url).status_code
    print(f"Статус код ответа сервера: {response_status_code}")
    print("=======================================")

    passenger_cars = browser.find_element(By.XPATH,"//span[@class='action-link' and @title='Легковые']")
    passenger_cars.click()
    current_url = browser.current_url
    print(f"Категория: {passenger_cars.text}")
    response_status_code = requests.get(current_url).status_code
    print(f"Статус код ответа сервера: {response_status_code}")
    print("=======================================")

    moto = browser.find_element(By.XPATH, "//span[@class='action-link' and @title='Мототехника']")
    moto.click()
    current_url = browser.current_url
    print(f"Категория: {moto.text}")
    response_status_code = requests.get(current_url).status_code
    print(f"Статус код ответа сервера: {response_status_code}")
    print("=======================================")

    water_transport = browser.find_element(By.XPATH, "//span[@class='action-link' and @title='Водный транспорт']")
    water_transport.click()
    current_url = browser.current_url
    print(f"Категория: {water_transport.text}")
    response_status_code = requests.get(current_url).status_code
    print(f"Статус код ответа сервера: {response_status_code}")
    print("=======================================")


finally:
    browser.quit()
