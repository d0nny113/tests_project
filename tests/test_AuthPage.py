import time

import pytest
from pages.AuthPage import AuthPage
from pages.PasswordRecoveryPage import PasswordRecoveryPage
from pages.RegisterPage import RegisterPage


@pytest.mark.parametrize('login', ['email@email.com'])
@pytest.mark.parametrize('password', ['email@email.com'])
def test_auth_by_email_negative(browser, login, password):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.navigate_to_login_by_email()
    auth_page.input_login(login)
    auth_page.input_password(password)
    auth_page.click_submit_button()
    assert auth_page.check_input_error()


def test_auth_by_login_positive(browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.navigate_to_login_by_login()
    auth_page.input_login('login')
    auth_page.input_password('password')
    auth_page.click_submit_button()


@pytest.mark.parametrize("auth_type", ['Номер', 'Почта', 'Логин', 'Лицевой счёт'])
def test_login_bar_types(browser, auth_type):
    auth_page = AuthPage(browser)
    auth_page.open()
    login_bar_options = auth_page.check_login_bar_types()
    assert auth_type in login_bar_options


@pytest.mark.parametrize('recovery_header', ['Восстановление пароля'])
def test_test(browser, recovery_header):
    auth_page = AuthPage(browser)
    recovery_page = PasswordRecoveryPage(browser)
    auth_page.open()
    auth_page.navigate_to_password_recovery_page()
    assert recovery_header in recovery_page.check_header()


@pytest.mark.parametrize('color', ['Orange'])
@pytest.mark.parametrize('auth_type', ['Почта'])
def test_(browser, color, auth_type):
    auth_page = AuthPage(browser)
    password_page = PasswordRecoveryPage(browser)
    auth_page.open()
    auth_page.input_login('donny11113@gmail.com')
    auth_page.input_password('vfksitD!990')
    time.sleep(10)
    auth_page.click_submit_button()
    time.sleep(10)


def test_drop(browser):
    auth_page = AuthPage(browser)
    register_page = RegisterPage(browser)
    auth_page.open()
    auth_page.navigate_to_register_page()
    print(register_page.region_list())















