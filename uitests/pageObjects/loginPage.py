from uitests.locators.loginPageLocators import logo, username_input, password_input, forgot_password_link, \
    login_button, page_title
from uitests.utils.utils import is_element_present, fill_input


# Methods used in login page
def check_elements_present(context):
    # Checking login page elements are displayed
    assert is_element_present(context, page_title), 'Page title is not present'
    assert is_element_present(context, login_button), 'Login button is not present'
    assert is_element_present(context, logo), 'Primer logo is not present'
    assert is_element_present(context, username_input), 'Username input is not present'
    assert is_element_present(context, password_input), 'Password input is not present'
    assert is_element_present(context, forgot_password_link), 'Forgot password link is not present'
