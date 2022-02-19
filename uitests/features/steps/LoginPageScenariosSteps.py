from behave import then, step
from uitests.pageObjects.loginPage import check_elements_present
from uitests.locators.loginPageLocators import page_title, username_input, login_button, \
    incorrect_credentials_message, forgot_password_link, request_link, email_input, password_input, reset_message
from uitests.utils.utils import is_element_present, click_element, fill_input


@then("I verify page is displayed properly")
def i_verify_page_is_correct(context):
    check_elements_present(context)
    page_title_text = context.driver.find_element_by_xpath(page_title).text
    assert page_title_text == 'Welcome back', 'Page title is not correct'


@step('I send "{username}" as username and "{password}" as password')
def i_send_credentials(context, username, password):
    assert is_element_present(context, username_input)
    fill_input(context, username_input, username)
    fill_input(context, password_input, password)


@step('I click login')
def i_click_login(context):
    click_element(context, login_button)


@then('I get incorrect credentials warning')
def i_get_warning(context):
    assert is_element_present(context, incorrect_credentials_message)


@step('I click Forgot password')
def i_click_forgot_pass(context):
    click_element(context, forgot_password_link)


@step('I provide "{email}" as email and proceed')
def i_give_email(context, email):
    fill_input(context, email_input, email)
    click_element(context, request_link)


@then('I verify reset email sent message')
def i_verify_reset_sent(context):
    assert is_element_present(context, reset_message)
    """if reset was working, this testcase could be
    expanded in order to check if an email is sent against
    a real email server"""
