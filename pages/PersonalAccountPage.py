from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class Locators:

    MARK = (By.XPATH, '//h3')


class PersonalAccountPage(BasePage):

    def check_personal_page(self):
        """ Метод возвращает True если находит заголовок h3
                    и текст в нем совпадает с текстом внутри ЛК """
        if self.wait_until_displayed_element(Locators.MARK).text == 'Учетные данные':
            return True

