from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    link2 = "http://google.com"
    browser = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')
    browser.get(link)
    browser.get(link2)
    browser.window_handles[0]
    time.sleep(5)
    browser.window_handles[1]
    time.sleep(5)
    #browser.get(link)
    #browser.execute_script("alert('Hello!');")
    #alert = browser.switch_to.alert
    #alert.accept()
    #time.sleep(10)
    #alert.accept()


    #browser.execute_script("prompt();")
    #alert = browser.switch_to.alert
    #alert_text = alert.text
    #print(alert_text*3)

    #confirm = browser.switch_to.alert
    #confirm.accept()
    #time.sleep(1)    
    #confirm.dismiss()

    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)

    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()