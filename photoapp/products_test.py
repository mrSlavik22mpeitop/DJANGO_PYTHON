from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
def test_products():
        try:
                browser = webdriver.Chrome()
                link = "http://127.0.0.1:8000/"
                browser.get(link)

                input1 = browser.find_elements_by_link_text("ТОВАР")[0].click()

                input2 = browser.find_elements_by_link_text("Добавить товар")[0].click()

                input3 = browser.find_element_by_id("id_product_name")
                input3.send_keys("mx-250")

                input4 = browser.find_element_by_id("id_product_company")
                input4.send_keys("Nikon")

                input5 = browser.find_element_by_id("id_price")
                input5.send_keys("100")

                input6 = browser.find_element_by_id("id_rating")
                input6.send_keys("4")

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

