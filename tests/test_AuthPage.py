import time
import pytest
from selenium.webdriver.common.by import By

from pages.AuthPage import AuthPage
from pages.PasswordRecoveryPage import PasswordRecoveryPageInputCode
from pages.PasswordRecoveryPage import PasswordRecoveryPageStepInputAccount
from pages.PasswordRecoveryPage import PasswordRecoveryPageSelectType
from pages.PersonalAccountPage import PersonalAccountPage
from pages.RegisterPage import RegisterPage
from settings import TestData


class TestAuthPage:

    @pytest.fixture()
    def auth_page(self, browser):
        auth_page = AuthPage(browser)
        auth_page.open()
        yield auth_page

    @pytest.fixture()
    def personal_account_page(self, browser):
        personal_account_page = PersonalAccountPage(browser)
        yield personal_account_page

    @pytest.mark.parametrize('auth_type', ['Номер', 'Почта', 'Логин', 'Лицевой счёт'])
    def test_auth_types(self, browser, auth_page, auth_type):
        """ Тест проверяет типы аутентификации согласно требованиям """

        auth_types = auth_page.check_login_bar_types()
        assert auth_type in auth_types

    def test_default_auth_type(self, browser, auth_page):
        """ Тест проверяет тип аутентификации по умолчанию """

        assert auth_page.check_login_bar_status() == 'Телефон'

    def test_auth_by_phone_positive(self, browser, auth_page, personal_account_page):
        """ Позитивный тест аутентификации при помощи телефона """

        auth_page.input_login(TestData.valid_phone_number)
        auth_page.input_password(TestData.valid_password)
        auth_page.click_submit_button()
        assert personal_account_page.check_personal_page()

    def test_auth_by_email_positive(self, browser, auth_page, personal_account_page):
        """ Позитивный тест аутентификации при помощи почты """

        auth_page.input_login(TestData.valid_email)
        auth_page.input_password(TestData.valid_password)
        auth_page.click_submit_button()
        assert personal_account_page.check_personal_page()

    def test_auth_by_login_positive(self, browser, auth_page, personal_account_page):
        """ Позитивный тест аутентификации при помощи логина """

        auth_page.input_login(TestData.valid_login)
        auth_page.input_password(TestData.valid_password)
        auth_page.click_submit_button()
        assert personal_account_page.check_personal_page()

    def test_auth_by_account_positive(self, browser, auth_page, personal_account_page):
        """ Позитивный тест аутентификации при помощи Лицевого Счета """

        auth_page.input_login(TestData.valid_account)
        auth_page.input_password(TestData.valid_password)
        auth_page.click_submit_button()
        assert personal_account_page.check_personal_page()

    def test_auth_tab_auto_change(self, browser, auth_page):
        """ Тест проверяет автоматическую смену таба выбора аутентификации
                           после ввода данных в поле ввода """

        auth_page.input_login(TestData.valid_email)
        auth_page.input_password(TestData.valid_password)
        assert auth_page.check_login_bar_status() == 'Почта'

    def test_error_message_after_invalid_auth(self, browser, auth_page):
        """ Тест проверяет сообщение после ввода неправильных данных для аутентификации """

        auth_page.input_login(TestData.invalid_phone_number)
        auth_page.input_password(TestData.invalid_password)
        auth_page.click_submit_button()
        assert auth_page.check_error_auth_text() == 'Неверный логин или пароль'

    def test_link_color_after_invalid_auth(self, browser, auth_page):
        """ Тест проверяет цвет линка 'Забыл пароль' после ввода неправильных данных для аутентификации"""

        auth_page.input_login(TestData.invalid_phone_number)
        auth_page.input_password(TestData.invalid_password)
        auth_page.click_submit_button()
        assert auth_page.check_forgot_password_link_color() == 'Orange'


