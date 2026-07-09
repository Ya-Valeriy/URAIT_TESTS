from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import url

# ФУНКЦИЯ ДЛЯ СТАРТА (Запускается один раз)

def start_home_page():
    global driver
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new") # Раскомментируйте, если нужен скрытый режим

    # ОБЯЗАТЕЛЬНО ДЛЯ HEADLESS:
    options.add_argument("--window-size=1920,1200")  # Задает стандартное FullHD разрешение
    options.add_argument("--disable-blink-features=AutomationControlled")  # Маскирует автоматизацию

    driver = webdriver.Chrome(options=options)
    driver.get(url.url_home_page_urait)
    time.sleep(5)


# ФУНКЦИЯ ДЛЯ ЗАКРЫТИЯ (Запускается в самом конце)

def close_browser():
    if driver:
        driver.quit()


# ФУНКЦИЯ ЛОГИРОВАНИЯ
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        # Добавляем аргументы filename и filemode
        filename='automation.log',
        filemode='w',  # 'a' — дополнять файл при каждом запуске, 'w' — перезаписывать
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'  # Защитит от кракозябр, если в логах будет русский текст
    )


# 1 --- ПРОВЕРКА ОТКРЫТИЯ ГЛАВНОЙ СТРАНИЦЫ ПО НАЛИЧИЮ ЗАГОЛОВКОВ

def test_home_page_open_successfully(words_to_find_home_page):

    # Заводим переменную с наименованием теста для передачи в журнал логов
    test_name = test_home_page_open_successfully.__name__

    # Ждем, пока body гарантированно появится на странице
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Получаем актуальный текст с открытой главной страницы сайта
    page_text = driver.find_element(By.TAG_NAME, "body").text.lower()

    # Ищем отсутствующие слова
    missing_words = [word for word in words_to_find_home_page if word.lower() not in page_text]

    # Проверяем результат
    if missing_words:
        logging.error(f"{test_name} - FAILED. Не найдены: {missing_words}")
        assert False, f"На странице не найдены слова: {missing_words}"

    logging.info(f"{test_name} - OK")


# 2 --- ПЕРЕХОД ПО ССЫЛКАМ ВЫПОЛНЯЕТСЯ УСПЕШНО

def test_following_links_successful(css_selector, selector_name, words_to_find):

    # Получаем имя текущей функции для логов
    test_name = test_following_links_successful.__name__
    wait = WebDriverWait(driver, 10)

    try:
        # Ожидаем и кликаем по кнопке
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        button.click()
        time.sleep(3)

        # Получаем текст страницы
        page_text = driver.find_element(By.TAG_NAME, "body").get_attribute("textContent").lower()

        # Ищем отсутствующие слова
        missing_words = [word for word in words_to_find if word.lower() not in page_text]

        # Проверяем результат без вызова assert
        if missing_words:
            logging.error(f"{test_name}, Переход по ссылке: {selector_name} - FAILED. Не найдены: {missing_words}")
        else:
            logging.info(f"{test_name}, Переход по ссылке: {selector_name} - OK")

    except WebDriverException as e:
        # Перехватываем ошибки Selenium (например, элемент не найден или не кликабелен)
        logging.error(f"{test_name}, Переход по ссылке: {selector_name} - FAILED. Ошибка Selenium: {e.msg}")

























