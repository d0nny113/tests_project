from selenium.common import NoSuchElementException
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AuthPageLocators:

    AUTH_LINK = 'https://b2c.passport.rt.ru'
    FIELD_USERNAME = (By.XPATH, '//input[@id="username"]')
    FIELD_USERNAME_PLACEHOLDER = (By.XPATH, '//span[@class="rt-input__placeholder"]')
    FIELD_PASSWORD = (By.XPATH, '//input[@id="password"]')
    BUTTON_ENTER = (By.XPATH, '//button[@id="kc-login"]')
    CONTAINER_LINK = (By.CSS_SELECTOR, '.tabs-input-container div')
    PHONE_LINK = (By.ID, 't-btn-tab-phone')
    EMAIL_LINK = (By.ID, 't-btn-tab-mail')
    LOGIN_LINK = (By.ID, 't-btn-tab-login')
    ACCOUNT_LINK = (By.ID, 't-btn-tab-ls')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[@id="forgot_password"]')
    REGISTER_LINK = (By.XPATH, '//a[@id="kc-register"]')
    HEADER_AUTHORIZATION = (By.CSS_SELECTOR, 'h1')
    MESSAGE_ERROR_SUBMIT = (By.CSS_SELECTOR, 'h1+p')


class AuthPage(BasePage):

    def check_header(self):
        """  Метод возвращает заголовок в правой части страницы """
        return self.wait_until_displayed_element(AuthPageLocators.HEADER_AUTHORIZATION).text

    def click_submit_button(self):
        """  Метод возвращает нажатие на кнопку Войти """
        return self.wait_until_clickable(AuthPageLocators.BUTTON_ENTER).click()

    def navigate_to_password_recovery_page(self):
        """  Метод возвращает переход на страницу восстановления пароля """
        return self.wait_until_clickable(AuthPageLocators.FORGOT_PASSWORD_LINK).click()

    def input_login(self, login):
        """  Метод возвращает ввод логина в поле username """
        return self.wait_until_clickable(AuthPageLocators.FIELD_USERNAME).send_keys(login)

    def input_password(self, password):
        """  Метод возвращает ввод пароля в поле password """
        return self.wait_until_clickable(AuthPageLocators.FIELD_PASSWORD).send_keys(password)

    def check_login_bar_types(self):
        """  Метод возвращает названия типов аутентификации в меню выбора  """
        login_bar = self.wait_until_clickable(AuthPageLocators.CONTAINER_LINK)
        login_types = ''.join(login_bar.text)
        return login_types

    def navigate_to_login_by_email(self):
        """  Метод возвращает выбор аутентификации при помощи Почты"""
        return self.wait_until_clickable(AuthPageLocators.EMAIL_LINK).click()

    def navigate_to_login_by_login(self):
        """  Метод возвращает выбор аутентификации при помощи Логина"""
        return self.wait_until_clickable(AuthPageLocators.LOGIN_LINK).click()

    def navigate_to_login_by_personal_account(self):
        """  Метод возвращает выбор аутентификации при помощи Лицевого Счёта"""
        return self.wait_until_clickable(AuthPageLocators.ACCOUNT_LINK).click()

    def navigate_to_login_by_phone(self):
        """  Метод возвращает выбор аутентификации при помощи Телефона """
        return self.wait_until_clickable(AuthPageLocators.PHONE_LINK).click()

    def check_username_placeholder(self):
        """  Метод возвращает название placeholder внутри поля ввода username """
        return self.wait_until_displayed_element(AuthPageLocators.FIELD_USERNAME_PLACEHOLDER).text

    def check_input_error(self):

        """  Метод проверяет сообщение об ошибке после ввода логина и пароля.
                  Возвращает True если оно есть False если его нет            """
        try:
            self.wait_until_displayed_element(AuthPageLocators.MESSAGE_ERROR_SUBMIT)
        except NoSuchElementException:
            return False
        return True

    def navigate_to_register_page(self):
        """  Метод возвращает переход на страницу регистрации """
        return self.wait_until_clickable(AuthPageLocators.REGISTER_LINK).click()

    def check_login_bar_status(self):
        """  Метод возвращает активный способ аутентификации """
        bar = self.wait_until_displayed_elements(AuthPageLocators.CONTAINER_LINK)
        for status in bar:
            if status.get_attribute('class') == 'rt-tab rt-tab--active':
                return status.text

    def check_forgot_password_color(self):
        """  Метод возвращает цвет линка 'Забыл пароль?' """
        link = self.wait_until_displayed_element(AuthPageLocators.FORGOT_PASSWORD_LINK)
        link_status = link.get_attribute('class')
        if link_status.find('animated') > 0:
            return 'Orange'
        else:
            return 'Gray'

