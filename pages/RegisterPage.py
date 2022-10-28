import time

from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.select import Select

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class RegisterPageLocators:

    HEADER_REGISTRATION = (By.CSS_SELECTOR, 'h1')
    FIELD_FIRST_NAME = (By.XPATH, '//input[@name="firstName"]')
    FIELD_LAST_NAME = (By.XPATH, '//input[@name="lastName"]')
    REGION_DROP_DOWN_LIST = (By.CSS_SELECTOR, '.rt-input-container.rt-select__input')
    REGION_DROP_DOWN_INSIDE = (By.CSS_SELECTOR, '.rt-select__list-wrapper.rt-select__list-wrapper--rounded')
    REGION_CHOSE = (By.XPATH, '//input[@name="region"]')
    FIELD_EMAIL_OR_PHONE = (By.XPATH, '//input[@id="address"]')
    FIELD_PASSWORD = (By.XPATH, '//input[@id="password"]')
    FIELD_PASSWORD_CONFIRM = (By.XPATH, '//input[@id="password-confirm"]')
    BUTTON_REGISTER = (By.XPATH, '//button[@name="register"]')


class RegisterPage(BasePage):

    def check_header(self):
        """  Метод возвращает заголовок в правой части страницы """
        return self.wait_until_displayed_element(RegisterPageLocators.HEADER_REGISTRATION).text

    def input_first_name(self, first_name):
        """  Метод возвращает ввод имени в поле имя """
        return self.wait_until_clickable(RegisterPageLocators.FIELD_FIRST_NAME).send_keys(first_name)

    def select_region(self, region_name):
        """  Метод возвращает выбор региона из выпадающего списка Регион, если он там есть
                    и ошибку с сообщением если региона нет в списке                       """
        self.wait_until_clickable(RegisterPageLocators.REGION_DROP_DOWN_LIST).click()
        region_drop_down = self.wait_until_clickable(RegisterPageLocators.REGION_DROP_DOWN_INSIDE)
        region_list = self.wait_until_clickable(RegisterPageLocators.REGION_DROP_DOWN_INSIDE).text.split('\n')
        if region_name not in region_list:
            raise NoSuchElementException(f'Региона {region_name } нет в списке')
        for region in region_drop_down.find_elements(By.CSS_SELECTOR, 'div'):
            try:
                if region.text == f'{region_name}':
                    region.click()
            except StaleElementReferenceException:
                pass

    def open_region_list(self):
        """  Метод возвращает раскрытие выпадающего списка регионы """
        return self.wait_until_clickable(RegisterPageLocators.REGION_DROP_DOWN_LIST).click()

    def region_list(self):
        """  Метод возвращает список регионов для выбора   """
        self.wait_until_clickable(RegisterPageLocators.REGION_DROP_DOWN_LIST).click()
        region_list = self.wait_until_clickable(RegisterPageLocators.REGION_DROP_DOWN_INSIDE).text.split('\n')
        region_list.pop(0)
        return region_list

    def input_last_name(self, last_name):
        """  Метод возвращает ввод фамилии в поле фамилия """
        return self.wait_until_clickable(RegisterPageLocators.FIELD_LAST_NAME).send_keys(last_name)

    def input_email_or_phone(self, email_or_phone):
        """  Метод возвращает ввод email или телефон в поле address """
        return self.wait_until_clickable(RegisterPageLocators.FIELD_EMAIL_OR_PHONE).send_keys(email_or_phone)

    def input_password(self, password):
        """  Метод возвращает ввод пароля в поле пароль """
        return self.wait_until_clickable(RegisterPageLocators.FIELD_PASSWORD).send_keys(password)

    def input_password_confirm(self, password_confirm):
        """  Метод возвращает ввод пароля в поле подтверждения пароля """
        return self.wait_until_clickable(RegisterPageLocators.FIELD_PASSWORD).send_keys(password_confirm)

    def submit_register(self):
        """  Метод возвращает нажатие на кнопку Зарегистрироваться """
        return self.wait_until_clickable(RegisterPageLocators.BUTTON_REGISTER).click()


