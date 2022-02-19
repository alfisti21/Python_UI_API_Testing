import allure
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from allure import attachment_type


def is_element_present(context, element):
    try:
        elements = WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.XPATH, element)))
        return True if elements else False
    except WebDriverException as e:
        # a screenshot will be taken whenever an element goes missing
        take_screenshot(context)
        context.driver.quit()


def click_element(context, element):
    if is_element_present(context, element):
        context.driver.find_element_by_xpath(element).click()


def fill_input(context, element, text):
    if is_element_present(context, element):
        context.driver.find_element_by_xpath(element).send_keys(text)


def take_screenshot(context):
    # using allure's capabilities to attach png screenshot whenever necessary
    allure.attach(context.driver.get_screenshot_as_png(), 'screenshot', attachment_type.PNG)
