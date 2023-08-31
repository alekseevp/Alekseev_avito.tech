from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time


def test_add_to_favorites():
    # Путь к ChromeDriver
    chromedriver_path = 'C:/chromedriver/chromedriver.exe'  # У автора не хочет работать PATH

    # Инициализация Selenium и ChromeDriver
    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Переход на страницу объявления
    driver.get("https://www.avito.ru/buynaksk/gruzoviki_i_spetstehnika/gaz_gazel_3302_bortovoy_2006_3411874134")

    try:
        # Добавление объявления в избранное
        add_to_favorites_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button"))
        )
        print("Кнопка 'Добавить в избранное' найдена")  # Для отслеживания выполнения дальше по коду
        time.sleep(2)   # Не нужно, я просто иначе глазами не успеваю проверять.

        add_to_favorites_button_text_before = add_to_favorites_button.text
        add_to_favorites_button.click()
        print("Кнопка 'Добавить в избранное' нажата")
        time.sleep(2)

        # Ожидание изменения текста на кнопке.
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.XPATH,
                                              "/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button"),
                                             "В избранном")
        )
        print("Текст кнопки изменен на 'В избранном'")
        time.sleep(2)

        # Проверка успешного добавления в избранное. Довольно простоватый метод отслеживания добавления, но соответствует параметрам задания.
        assert add_to_favorites_button.text == "В избранном"
        print("Объявление успешно добавлено в избранное")
        time.sleep(2)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Закрытие браузера
        driver.quit()


# Запуск теста
test_add_to_favorites()
