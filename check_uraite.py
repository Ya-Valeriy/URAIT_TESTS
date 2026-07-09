import url
from tests_urait import (start_home_page, close_browser, setup_logging,

                         test_following_links_successful,
                         test_home_page_open_successfully,
                         test_clicking_before_adding_item_cart,
                         test_item_added_cart)
import locators
import words_to_find

# 1. Запускаем браузер один раз перед всеми тестами
start_home_page()
# 2 Запускаем логирование
setup_logging()
try:
    # Проверка открытия главной страницы по факту открытия заголовков
    test_home_page_open_successfully(words_to_find.words_to_find_home_page)

    # Проверка перехода по ссылке "Каталог"
    test_following_links_successful(locators.button_catalog, "Каталог", words_to_find.words_to_find_catalog)

    # Проверка перехода по ссылке "Преподавателям"
    test_following_links_successful(locators.button_to_teachers, "Преподавателям", words_to_find.words_to_find_to_teachers)

    # Проверка перехода по ссылке "Студентам"
    test_following_links_successful(locators.button_to_students, "Студентам", words_to_find.words_to_find_to_students)

    # Проверка перехода по ссылке "Учебным заведениям"
    test_following_links_successful(locators.button_educational_institutions, "Учебным заведениям", words_to_find.words_to_find_educational_institutions)

    # Проверка перехода по ссылке "Обучение преподавателей"
    test_following_links_successful(locators.button_teacher_training, "Обучение преподавателей", words_to_find.words_to_find_teacher_training)

    # Проверка по ссылке "Новости"
    test_following_links_successful(locators.button_news, "Новости", words_to_find.words_to_find_news)

    # Проверка перехода по ссылке "Помощь"
    test_following_links_successful(locators.button_help, "Помощь", words_to_find.words_to_find_help)

finally:
    # 3. Закрываем браузер после выполнения всех тестов
    close_browser()



