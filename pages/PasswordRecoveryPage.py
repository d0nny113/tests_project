from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:

    FIELD_USERNAME = (By.XPATH, '//input[@id="username"]')
    FIELD_USERNAME_PLACEHOLDER = (By.XPATH, '//span[@class="rt-input__placeholder"]')
    BUTTON_PROCEED = (By.XPATH, '//button[@id="reset"]')
    BUTTON_BACK = (By.XPATH, '//button[@id="reset-back"]')
    CONTAINER_LINK = (By.XPATH, '//div[@class="rt-tabs rt-tabs--orange tabs-input-container__tabs"]')
    HEADER_RECOVERY = (By.CSS_SELECTOR, 'h1')
    PHONE_LINK = (By.ID, 't-btn-tab-phone')
    EMAIL_LINK = (By.ID, 't-btn-tab-mail')
    LOGIN_LINK = (By.ID, 't-btn-tab-login')
    ACCOUNT_LINK = (By.ID, 't-btn-tab-ls')


class PasswordRecoveryPage(BasePage):

    def check_header(self):
        """  Метод возвращает заголовок в правой части страницы """
        return self.wait_until_displayed_element(PasswordRecoveryPageLocators.HEADER_RECOVERY).text

    def navigate_to_recovery_by_email(self):
        """  Метод возвращает выбор восстановления пароля при помощи Почты"""
        return self.wait_until_clickable(PasswordRecoveryPageLocators.EMAIL_LINK).click()

    def navigate_to_recovery_by_login(self):
        """  Метод возвращает выбор восстановления пароля при помощи Логина"""
        return self.wait_until_clickable(PasswordRecoveryPageLocators.LOGIN_LINK).click()

    def navigate_to_recovery_by_personal_account(self):
        """  Метод возвращает выбор восстановления пароля при помощи Лицевого Счёта"""
        return self.wait_until_clickable(PasswordRecoveryPageLocators.ACCOUNT_LINK).click()

    def navigate_to_recovery_by_phone(self):
        """  Метод возвращает выбор восстановления пароля при помощи Телефона """
        return self.wait_until_clickable(PasswordRecoveryPageLocators.PHONE_LINK).click()

    def click_button_proceed(self):
        """  Метод возвращает нажатие на кнопку Продолжить """
        return self.wait_until_clickable(PasswordRecoveryPageLocators.BUTTON_PROCEED).click()

    def click_button_back(self):
        """  Метод возвращает нажатие на кнопку "Вернуться назад" """
        return self.wait_until_clickable(PasswordRecoveryPageLocators.BUTTON_BACK).click()
