from behave import *
from features.pages.login_page import LoginPage
from webdriver import Driver

use_step_matcher("re")


@given("I am on login page")
def step_impl_open_login_page(context):
    """
    :type context: behave.runner.Context
    """
    context.driver = Driver()
    context.loginpage = LoginPage(context.driver)
    context.loginpage.load_login_page()
    context.loginpage.verify_on_login_page()


@when("I type correct username in the username field")
def step_impl_type_correct_username(context):
    """
    :type context: behave.runner.Context
    """
    context.loginpage.fill_correct_username()


@step("I type correct password in the password field")
def step_impl_type_password(context):
    """
    :type context: behave.runner.Context
    """
    context.loginpage.fill_correct_pwd()


@step("I click the Login button")
def step_impl_click_button(context):
    """
    :type context: behave.runner.Context
    """
    context.loginpage.click_submit_btn()


@then("I am logged in")
def step_impl_validate_logged_in(context):
    """
    :type context: behave.runner.Context
    """
    context.loginpage.verify_logged_in()
    context.loginpage.close_website()

@when("I type wrong username in the username field")
def step_impl_type_wrong_username(context):
    """
    :type context: behave.runner.Context
    """
    context.loginpage.fill_incorrect_username()


@step("I type any password in the password field")
def step_impl_type_random_text(context):
    """
    :type context: behave.runner.Context
    """
    context.loginpage.fill_random_pwd()


@then("I see error notification")
def step_impl_validate_error_notification(context):
    """
    :type context: behave.runner.Context
    """
    context.loginpage.verify_error_notification_is_displayed()
    context.loginpage.close_website()
