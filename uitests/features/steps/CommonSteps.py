from behave import step, given
from selenium import webdriver
from uitests.utils.utils import take_screenshot
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# Here we will define steps that are used by lots of feature files or scenarios
@given('I access "{url}" with {browser}')
def i_access_url(context, url, browser):
    # We set-up the driver with the desired headless option
    chrome_options = Options()
    firefox_options = FirefoxOptions()
    chrome_options.add_argument("--headless")
    firefox_options.add_argument("--headless")
    if browser == "Chrome":
        context.driver = webdriver.Chrome(chrome_options=chrome_options)
    elif browser == "Firefox":
        context.driver = webdriver.Firefox(firefox_options=firefox_options)
    context.driver.get(url)


@step('I quit the driver')
def i_quit_driver(context):
    take_screenshot(context)  # take a screenshot at the end of each step - optional
    context.driver.quit()
