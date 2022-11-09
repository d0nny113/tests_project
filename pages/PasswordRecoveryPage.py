from selenium.common import NoSuchElementException
from selenium.webdriver import Keys

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LocatorsInputAccount:

    FIELD_USERNAME = (By.XPATH, '//input[@id="username"]')
    FIELD_USERNAME_PLACEHOLDER = (By.XPATH, '//span[@class="rt-input__placeholder"]')
    BUTTON_PROCEED = (By.XPATH, '//button[@id="reset"]')
    BUTTON_BACK = (By.XPATH, '//button[@id="reset-back"]')
    CONTAINER_LINK = (By.CSS_SELECTOR, '.tabs-input-container div')
    HEADER_RECOVERY = (By.CSS_SELECTOR, 'h1')
    PHONE_LINK = (By.ID, 't-btn-tab-phone')
    EMAIL_LINK = (By.ID, 't-btn-tab-mail')
    LOGIN_LINK = (By.ID, 't-btn-tab-login')
    ACCOUNT_LINK = (By.ID, 't-btn-tab-ls')


class LocatorsSelectType:

    HEADER_RECOVERY = (By.CSS_SELECTOR, 'h1')
    RADIO_GROUP = (By.CSS_SELECTOR, '.rt-radio.rt-radio--orange')
    RADIO_TEXT = (By.XPATH, '//input[@class="rt-radio__input"]')
    RADIO_EMAIL = (By.XPATH, '//input[@value="email"]')
    BUTTON_PROCEED = (By.XPATH, '//button[@type="submit"]')


class LocatorsInputCode:

    RECOVERY_TEXT = (By.XPATH, '//p[@class="card-container__desc"]')
    BUTTON_RESEND = (By.XPATH, '//button[@name="otp_resend_code"]')
    BUTTON_BACK = (By.XPATH, '//button[@name="cancel_reset"]')
    SIX_NUMBERS = (By.XPATH, '//div[@class="sdi-container sdi-container--medium"]')


class PasswordRecoveryPageStepInputAccount(BasePage):

    def check_header(self):
        """  Метод возвращает заголовок в правой части страницы """
        return self.wait_until_displayed_element(LocatorsInputAccount.HEADER_RECOVERY).text

    def navigate_to_recovery_by_email(self):
        """  Метод возвращает выбор восстановления пароля при помощи Почты"""
        return self.wait_until_clickable(LocatorsInputAccount.EMAIL_LINK).click()

    def navigate_to_recovery_by_login(self):
        """  Метод возвращает выбор восстановления пароля при помощи Логина"""
        return self.wait_until_clickable(LocatorsInputAccount.LOGIN_LINK).click()

    def navigate_to_recovery_by_personal_account(self):
        """  Метод возвращает выбор восстановления пароля при помощи Лицевого Счёта"""
        return self.wait_until_clickable(LocatorsInputAccount.ACCOUNT_LINK).click()

    def navigate_to_recovery_by_phone(self):
        """  Метод возвращает выбор восстановления пароля при помощи Телефона """
        return self.wait_until_clickable(LocatorsInputAccount.PHONE_LINK).click()

    def button_submit_click(self):
        """  Метод возвращает нажатие на кнопку Продолжить """
        return self.wait_until_clickable(LocatorsInputAccount.BUTTON_PROCEED).click()

    def click_button_back(self):
        """  Метод возвращает нажатие на кнопку "Вернуться назад" """
        return self.wait_until_clickable(LocatorsInputAccount.BUTTON_BACK).click()

    def input_username(self, data):
        """  Метод возвращает ввод в поле username """
        return self.wait_until_clickable(LocatorsInputAccount.FIELD_USERNAME).send_keys(data)

    def check_login_bar_status(self):
        """  Метод возвращает активный способ аутентификации """
        type_bar = self.wait_until_displayed_elements(LocatorsInputAccount.CONTAINER_LINK)
        for status in type_bar:
            if status.get_attribute('class') == 'rt-tab rt-tab--small rt-tab--active':
                return status.text


class PasswordRecoveryPageSelectType(BasePage):

    def button_submit_click(self):
        """  Метод возвращает нажатие на кнопку Продолжить """
        return self.wait_until_clickable(LocatorsSelectType.BUTTON_PROCEED).click()

    def select_recovery_type(self, value):
        """  Метод возвращает выбор восстановления пароля """

        buttons = self.wait_until_displayed_elements(LocatorsSelectType.RADIO_GROUP)
        if not any(i.find_element(By.CSS_SELECTOR, 'input').get_property('value') == value for i in buttons):
            raise NoSuchElementException('Способ восстановления отсутствует в списке')
        for button in buttons:
            if button.find_element(By.CSS_SELECTOR, 'input').get_property('value') == value:
                button.find_element(By.CLASS_NAME, 'rt-radio__circle').click()

    def check_recovery_types(self):
        """  Метод возвращает список вариантов выбора восстановления пароля """
        types = []
        buttons = self.wait_until_displayed_elements(LocatorsSelectType.RADIO_GROUP)
        for button in buttons:
            types.append(button.find_element(By.CSS_SELECTOR, 'input').get_property('value'))

        return types


class PasswordRecoveryPageInputCode(BasePage):

    def input_code_numbers(self, code: str):
        """  Метод возвращает ввод шестизначного кода из SMS в поля ввода """
        code = code.split(' ')
        self.driver.find_element(By.CSS_SELECTOR, 'input:focus').send_keys(code[0])
        self.driver.find_element(By.CSS_SELECTOR, 'input:focus').send_keys(code[1])
        self.driver.find_element(By.CSS_SELECTOR, 'input:focus').send_keys(code[2])
        self.driver.find_element(By.CSS_SELECTOR, 'input:focus').send_keys(code[3])
        self.driver.find_element(By.CSS_SELECTOR, 'input:focus').send_keys(code[4])
        self.driver.find_element(By.CSS_SELECTOR, 'input:focus').send_keys(code[5])
