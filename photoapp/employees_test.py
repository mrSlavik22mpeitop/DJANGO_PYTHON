from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
def test_employees():
        try:
                browser = webdriver.Chrome()
                link = "http://127.0.0.1:8000/"
                browser.get(link)

                input1 = browser.find_elements_by_link_text("СОТРУДНИК")[0].click()

                input2 = browser.find_elements_by_link_text("Добавить сотрудника")[0].click()

                input3 = browser.find_element_by_id("id_first_name")
                input3.send_keys("Максим")

                input4 = browser.find_element_by_id("id_second_name")
                input4.send_keys("Иванов")

                input5 = browser.find_element_by_id("id_email")
                input5.send_keys("amdin@mail.ru")

                input6 = browser.find_element_by_id("id_phone")
                input6.send_keys("+79265489274")

                input7 = browser.find_element_by_id("id_office_code")
                input7.send_keys("100")

                input8 = browser.find_element_by_id("id_position")
                input8.send_keys("Продавец")


                button = browser.find_element_by_tag_name("button")
                button.click()
                # Проверяем, что смогли зарегистрироваться
                # ждем загрузки страницы
                welcome_text_elt = browser.find_element_by_tag_name("h1")
                # находим элемент, содержащий текст
                # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
                # записываем в переменную welcome_text текст из элемента welcome_text_elt
                welcome_text = welcome_text_elt.text
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
                time.sleep(10)
            # закрываем браузер после всех манипуляций
                browser.quit()

