import time
import pytest


from pages.AuthPage import AuthPage
from pages.PasswordRecoveryPage import PasswordRecoveryPageInputCode
from pages.PasswordRecoveryPage import PasswordRecoveryPageStepInputAccount
from pages.PasswordRecoveryPage import PasswordRecoveryPageSelectType
from pages.PasswordRecoveryPage import PasswordRecoveryPageNewPassword
from pages.PersonalAccountPage import PersonalAccountPage
from pages.RegisterPage import RegisterPage
from settings import TestData


@pytest.fixture()
def auth_page(browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    yield auth_page


@pytest.fixture()
def personal_account_page(browser):
    personal_account_page = PersonalAccountPage(browser)
    yield personal_account_page


@pytest.fixture()
def rec_step_1(browser):
    password_recovery_page_step_1 = PasswordRecoveryPageStepInputAccount(browser)
    yield password_recovery_page_step_1


@pytest.fixture()
def rec_step_2(browser):
    password_recovery_page_step_2 = PasswordRecoveryPageSelectType(browser)
    yield password_recovery_page_step_2


@pytest.fixture()
def rec_step_3(browser):
    password_recovery_page_step_3 = PasswordRecoveryPageInputCode(browser)
    yield password_recovery_page_step_3


@pytest.fixture()
def rec_step_4(browser):
    password_recovery_page_step_4 = PasswordRecoveryPageNewPassword(browser)
    yield password_recovery_page_step_4


@pytest.fixture()
def register_page(browser):
    register_page = RegisterPage(browser)
    yield register_page


class TestAuthPage:

    @pytest.mark.parametrize('auth_type', ['Номер', 'Почта', 'Логин', 'Лицевой счёт'])
    def test_auth_types(self, browser, auth_page, auth_type):
        """ Тест проверяет типы аутентификации согласно требованиям соответствует тест кейсу А1 """

        auth_types = auth_page.check_login_bar_types()
        assert auth_type in auth_types

    def test_default_auth_type(self, browser, auth_page):
        """ Тест проверяет тип аутентификации по умолчанию соответствует тест кейсу А2"""

        assert auth_page.check_login_bar_status() == 'Номер'

    @pytest.mark.parametrize('auth_type', [TestData.valid_phone_number, TestData.valid_email, TestData.valid_login,
                                           TestData.valid_account])
    @pytest.mark.parametrize('password', [TestData.valid_password])
    def test_auth_by_phone_positive(self, browser, auth_page, personal_account_page, auth_type, password):
        """ Позитивный тест аутентификации соответствует тест кейсам А3 - А6"""
        auth_page.input_login(auth_type)
        auth_page.input_password(password)
        time.sleep(15) # ожидание для ввода Captcha
        auth_page.click_submit_button()
        assert personal_account_page.check_personal_page()

    @pytest.mark.parametrize('auth_type,bar_status',
                             [(TestData.valid_email, 'Почта'), (TestData.valid_phone_number, 'Номер'),
                              (TestData.valid_login, 'Логин'), (TestData.valid_account, 'Лицевой счёт')])
    def test_auth_tab_auto_change(self, browser, auth_page, auth_type, bar_status):
        """ Тест проверяет автоматическую смену таба выбора аутентификации
                           после ввода данных в поле ввода соответствует тест кейсу А8 - А11 """

        auth_page.input_login(auth_type)
        auth_page.input_password(TestData.valid_password)
        assert auth_page.check_login_bar_status() == bar_status

    @pytest.mark.parametrize('auth_type', [TestData.valid_phone_number, TestData.valid_email, TestData.valid_login,
                                           TestData.valid_account])
    @pytest.mark.parametrize('password', [TestData.invalid_password])
    def test_error_message_after_invalid_auth(self, browser, auth_page, auth_type, password):
        """ Тест проверяет сообщение после ввода неправильных данных для аутентификации
                                                                  соответствует тест кейсу А12 - A 15"""

        auth_page.input_login(TestData.invalid_phone_number)
        auth_page.input_password(TestData.invalid_password)
        auth_page.click_submit_button()
        assert auth_page.check_error_auth_text() == 'Неверный логин или пароль'

    @pytest.mark.parametrize('auth_type', [TestData.valid_phone_number, TestData.valid_email, TestData.valid_login,
                                           TestData.valid_account])
    @pytest.mark.parametrize('password', [TestData.invalid_password])
    def test_link_color_after_invalid_auth(self, browser, auth_page, auth_type, password):
        """ Тест проверяет цвет линка 'Забыл пароль' после ввода неправильных данных для аутентификации
                                                                           соответствует тест кейсу А16 - А19"""

        auth_page.input_login(TestData.invalid_phone_number)
        auth_page.input_password(TestData.invalid_password)
        auth_page.click_submit_button()
        assert auth_page.check_forgot_password_link_color() == 'Orange'


class TestPasswordRecoveryPage:

    @pytest.mark.parametrize('recovery_type', ['Номер', 'Почта', 'Логин', 'Лицевой счёт'])
    def test_recovery_types(self, browser, auth_page, rec_step_1, recovery_type):
        """ Тест проверяет типы восстановления пароля согласно требованиям соответствует тест кейсу В1"""
        auth_page.navigate_to_password_recovery_page()
        recovery_types = rec_step_1.check_recovery_bar_types()
        assert recovery_type in recovery_types

    def test_default_recovery_type(self, browser, auth_page, rec_step_1):
        """ Тест проверяет тип восстановления пароля по умолчанию соответствует тест кейсу В2 """
        auth_page.navigate_to_password_recovery_page()
        assert rec_step_1.check_recovery_bar_status() == 'Номер'

    def test_recovery_password_methods(self, browser, auth_page, rec_step_1, rec_step_2):
        """ Тест проверяет способы восстановления пароля, так как нет возможности связаться с разработчиком
                    в тесте присутствует ожидание для ввода Captcha соответствует тест кейсу В3 """

        auth_page.navigate_to_password_recovery_page()
        rec_step_1.input_username(TestData.valid_phone_number)
        time.sleep(10)  # ожидание для ввода Captcha
        rec_step_1.button_submit_click()
        assert rec_step_2.check_recovery_types() == TestData.recovery_methods

    @pytest.mark.parametrize('rec_type',
                             [TestData.valid_phone_number, TestData.valid_email,
                              TestData.valid_login, TestData.valid_account])
    def test_rec_password_by_sms_positive(self, browser, auth_page, rec_step_1, rec_step_2,
                                          rec_step_3, rec_step_4, rec_type):
        """ Тест проверяет восстановления пароля при помощи SMS, так как нет возможности связаться с разработчиком
         в тесте присутствует ожидание для ввода Captcha и кода для презентации работоспособности теста
                                                                                соответствует тест кейсу В4 - B7 """

        auth_page.navigate_to_password_recovery_page()
        rec_step_1.input_username(rec_type)
        time.sleep(10)  # ожидание для ввода Captcha
        rec_step_1.button_submit_click()
        rec_step_2.select_recovery_type('sms')
        rec_step_2.button_submit_click()
        time.sleep(15)  # ожидание для ввода кода из SMS
        rec_step_4.input_new_password(TestData.valid_new_password)
        rec_step_4.input_new_password_confirm(TestData.valid_new_password)
        rec_step_4.button_save_submit()
        assert auth_page.check_header() == 'Авторизация'

    @pytest.mark.parametrize('rec_type',
                             [TestData.valid_phone_number, TestData.valid_email,
                              TestData.valid_login, TestData.valid_account])
    def test_rec_password_by_sms_positive_v2(self, browser, auth_page, rec_step_1, rec_step_2,
                                             rec_step_3, rec_step_4, rec_type):
        """ Тест проверяет восстановления пароля при помощи SMS. Это его вторая версия, как бы он выглядел при
         возможности работы в тестовом окружении, тест отправляет код-заглушку, вместо кода из смс и не ждет
            ввод Captcha """

        auth_page.navigate_to_password_recovery_page()
        rec_step_1.input_username(rec_type)
        rec_step_1.button_submit_click()
        rec_step_2.select_recovery_type('sms')
        rec_step_2.button_submit_click()
        rec_step_3.input_code_numbers('123456')
        rec_step_4.input_new_password(TestData.valid_new_password)
        rec_step_4.input_new_password_confirm(TestData.valid_password)
        rec_step_4.button_save_submit()
        assert auth_page.check_header() == 'Авторизация'

    @pytest.mark.parametrize('rec_type',
                             [TestData.valid_phone_number, TestData.valid_email,
                              TestData.valid_login, TestData.valid_account])
    def test_rec_password_by_email_positive(self, browser, auth_page, rec_step_1, rec_step_2, rec_step_3,
                                            rec_step_4, rec_type):
        """ Тест проверяет восстановления пароля при помощи EMAIL, так как нет возможности связаться с разработчиком
         в тесте присутствует ожидание для ввода Captcha и кода для презентации работоспособности теста
                                                                            соответствует тест кейсу В8 - B11"""

        auth_page.navigate_to_password_recovery_page()
        rec_step_1.input_username(rec_type)
        time.sleep(10)  # ожидание для ввода Captcha
        rec_step_1.button_submit_click()
        rec_step_2.select_recovery_type('email')
        rec_step_2.button_submit_click()
        time.sleep(15)  # ожидание для ввода кода из SMS
        rec_step_4.input_new_password(TestData.valid_new_password)
        rec_step_4.input_new_password_confirm(TestData.valid_new_password)
        rec_step_4.button_save_submit()
        assert auth_page.check_header() == 'Авторизация'


class TestRegisterPage:
    @pytest.mark.parametrize('reg_type', [TestData.valid_phone_number, TestData.valid_email])
    def test_register_positive(self, browser, auth_page, register_page, rec_step_3, personal_account_page, reg_type):
        """ Позитивный тест регистрации нового пользователя на платформе, так как нет возможности связаться с
          разработчиком и получить код-заглушку для ввода, в тесте присутствует ожидание ввода кода для презентации
               работоспособности теста соответствует тест кейсу Р1 """

        auth_page.navigate_to_register_page()
        register_page.input_first_name(TestData.valid_firs_name)
        register_page.input_last_name(TestData.valid_last_name)
        register_page.select_region('Алтай Респ')
        register_page.input_email_or_phone(reg_type)
        register_page.input_password(TestData.vlid_reg_pass)
        register_page.input_password_confirm(TestData.vlid_reg_pass)
        register_page.submit_register()
        time.sleep(30)  # ожидание для ввода кода
        assert personal_account_page.check_personal_page()

    def test_register_positive_v2(self, browser, auth_page, register_page, rec_step_3, personal_account_page):
        """ Позитивный тест регистрации нового пользователя на платформе, так бы тест выглядел для работы в тестовой
                                                     среде, где есть возможность ввода кода-заглушки от разработчика"""

        auth_page.navigate_to_register_page()
        register_page.input_first_name(TestData.valid_firs_name)
        register_page.input_last_name(TestData.valid_last_name)
        register_page.select_region('Алтай Респ')
        register_page.input_email_or_phone(TestData.valid_reg_email)
        register_page.input_password(TestData.vlid_reg_pass)
        register_page.input_password_confirm(TestData.vlid_reg_pass)
        register_page.submit_register()
        rec_step_3.input_code_numbers('123456')
        assert personal_account_page.check_personal_page()

    @pytest.mark.parametrize('firs_name', ['John', '12345', '!@#$%', 'Аа'])
    @pytest.mark.parametrize('last_name', ['Dough', '6789', '^&*()_', 'Бб'])
    @pytest.mark.parametrize('email_or_phone', ['email.ee', 'email@email', '^&*()_', 'Abcd', '123456', '1@1.1'])
    @pytest.mark.parametrize('password', ['qwertyu', 'qwertyuio', 'абвгдеёжзик'])
    def test_register_negative(self, browser, auth_page, register_page, rec_step_3, personal_account_page, firs_name,
                               last_name, email_or_phone, password):
        """ Негативный тест регистрации нового пользователя на платформе, соответствует тест кейсу Р2 """

        auth_page.navigate_to_register_page()
        register_page.input_first_name(firs_name)
        register_page.input_last_name(last_name)
        register_page.select_region('Алтай Респ')
        register_page.input_email_or_phone(email_or_phone)
        register_page.input_password(password)
        register_page.input_password_confirm(password)
        register_page.submit_register()
        assert register_page.check_errors() is False



