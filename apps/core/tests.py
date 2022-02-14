from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import keys
# from selenium.webdriver.chrome.options import Options
import time

# para efetuar os testes utilizar python manage.py test apps.core.tests

# driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)


# driver.get('http://127.0.0.1:8000/')
# assert "Game Mania" in driver.title
# driver.get("https://google.com/")
# print(driver.title)
# driver.quit()

class Hosttest(LiveServerTestCase):

    # def testhomepage(self):
    #     # Executa as ações mas em modo oculto
    #     # options = Options()
    #     # options.headless = True

    #     # driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
    #     driver = webdriver.Chrome("/usr/bin/chromedriver")
    #     time.sleep(5)
    #     driver.get('http://127.0.0.1:8000/')
    #     # driver.get('https://www.google.com.br/')
    #     print(driver.title)
    #     assert "Google" in driver.title

    def LoginFormTest(self):
        driver = webdriver.Chrome("/usr/bin/chromedriver")
        driver.get('http://127.0.0.1:8000/contas/login/')

        time.sleep(3)

        user_name = driver.find_element_by_id('username')
        user_password = driver.find_element_by_id('password')
        submit = driver.find_element_by_id('id_submit')

        user_name.send_keys('admin')
        user_password.send_keys('1234')

        time.sleep(3)

        submit.send_keys(keys.RETURN)

        assert 'admin' in driver.page_source()
