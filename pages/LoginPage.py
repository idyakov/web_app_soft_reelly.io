from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from support.logger import logger


class LoginPage(Page):
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[class="login-button w-button"]')
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    REELLY_EMAIL = (By.CSS_SELECTOR, "[id*='email-2']")  # input email
    REELLY_PASSWORD = (By.CSS_SELECTOR, "[id*='field']")  # input password
    CLICK_SETTINGS = (By.XPATH, "//div[contains(@class, 'mobile-top-menu') and text()='Menu']")
    CLICK_EDIT_PROFILE = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Edit profile']")
    INPUT_FIELD_VERIFICATION = (
        By.XPATH, "//input[contains(@class, 'field-form-block w-input') and contains(@name, 'Languages')]")
    INPUT_NAME = (
        By.XPATH, "//input[contains(@class, 'input w-input') and contains(@placeholder, 'First and Last name')]")
    INPUT_PHONE = (By.XPATH, "//input[contains(@class, 'input phone w-input') and contains(@id, 'phone2')]")
    INPUT_PWD = (By.XPATH, "//input[contains(@class, 'input w-input') and contains(@id, 'field')]")
    INPUT_COMP_WEB = (By.XPATH, "//input[contains(@class, 'input w-input') and contains(@id, 'Company-website')]")
    #   INPUT_ROLE = (By.XPATH, "//select[contains(@id, 'Role')]/option[@value='Developer']")
    MENU_COUNTRY = (By.XPATH, "//select[contains(@id, 'country-select')]")
    MENU_COMP_SIZE = (By.XPATH, "//select[contains(@id, 'Agents-amount-2')]")
    CLICK_SAVE = (By.XPATH, "//div[contains(text(), 'Save changes')]")
    CLICK_CLOSE = (By.XPATH, "//div[contains(@class, 'profile-button') and contains(., 'Close')]")
    CLICK_CREATE_ACCOUNT = (By.XPATH, "//a[contains(@class, 'login-button w-button') and text()='Create account']")
    MENU_ROLE = (By.XPATH, "//select[contains(@id, 'Role')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # def click_save_changes(self):
    #     # Get the second element that matches the XPath
    #     elements = self.driver.find_elements(*self.CLICK_SAVE)
    #     if len(elements) > 1:
    #         elements[1].click()
    #     else:
    #         raise Exception("The second 'Save changes' button was not found.")

    # def __init__(self, driver):
    #     super().__init__(driver)
    # #     self.default_pw = 'Password'
    #
    # def click_sign_in(self):
    #     self.click(*self.CONTINUE_BUTTON)

    # def input_credentials(self):
    #     self.input_text('dyak.ilya@gmail.com', *self.REELLY_EMAIL)  #input your own registered email
    #     self.input_text('XrvzakG!E4i@Zzh', *self.REELLY_PASSWORD)  #input your own registered password
    #
    # def click_on_settings(self):
    #     self.click(*self.CLICK_SETTINGS)
    #
    # def edit_profile(self):
    #     WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located(self.CLICK_EDIT_PROFILE)
    #     ).click()

    def input_fields(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_NAME)
        )
        self.input_text('Dmitri Mendeleev', *self.INPUT_NAME)

    def input_fields_phone(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_PHONE)
        )
        self.input_text('88875773', *self.INPUT_PHONE)

    def input_fields_pwd(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_PWD)
        )
        self.input_text('trumpampam', *self.INPUT_PWD)

    def input_fields_comp_web(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_COMP_WEB)
        )
        self.input_text('trump@gmail.com', *self.INPUT_COMP_WEB)

    def dropdown_menu_role(self):
        dropdown_menu_1 = self.find_element(*self.MENU_ROLE)
        select = Select(dropdown_menu_1)
        logger.info(f'verification_of_dropdown_list - {select}')
        select.select_by_value('Developer')

    def dropdown_menu_country(self):
        dropdown_menu_1 = self.find_element(*self.MENU_COUNTRY)
        select = Select(dropdown_menu_1)
        logger.info(f'verification_of_dropdown_list - {select}')
        select.select_by_value('United States of America')

    def dropdown_menu_comp_size(self):
        dropdown_menu_1 = self.find_element(*self.MENU_COMP_SIZE)
        select = Select(dropdown_menu_1)
        logger.info(f'verification_of_dropdown_list - {select}')
        select.select_by_value('I work alone')

    def click_create_account(self):
        self.click(self.CLICK_CREATE_ACCOUNT)

    def verify_page(self, expected_url):
        logger.info(f'Verified expected url - {expected_url}')
        print(expected_url)
        self.wait.until(EC.url_contains(expected_url), message=f'URL verified')

    def verify_the_button(self, create_account_button):
        create_account_button = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Create account')]")
        # Verify the button is visible
        assert create_account_button.is_displayed(), "Create account button is not visible"
        assert create_account_button.text == "Create account", (f"Button text is incorrect. Expected 'Create account', "
                                                                f"got '{create_account_button.text}'")
    # def click_on_close(self):
    #     # Get the second element that matches the XPath
    #     elements = self.driver.find_elements(*self.CLICK_CLOSE)
    #     if len(elements) > 1:
    #         elements[1].click()
    #     else:
    #         raise Exception("The second 'Close' button was not found.")
