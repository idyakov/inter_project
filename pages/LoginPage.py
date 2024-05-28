from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage(Page):
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[class="login-button w-button"]')
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    SING_IN_POPUP = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    REELLY_EMAIL = (By.CSS_SELECTOR, "[id*='email-2']")  # input email
    REELLY_PASSWORD = (By.CSS_SELECTOR, "[id*='field']")  # input password
    CLICK_SETTINGS = (By.XPATH, "//div[contains(@class, 'menu-button-text') and text()='Settings']")
    CLICK_EDIT_PROFILE = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Edit profile']")
    TARGET_VERIFY_ACCOUNT = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    # click button SIgn in with password
    TARGET_NAME_VERIFICATION = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    INPUT_FIELD = (By.CSS_SELECTOR, "[id*='Languages']")
    CLICK_SAVE = (By.XPATH, "//div[contains(@wized, 'saveButtonProfile') and text()='Save changes']")
    def __init__(self, driver):
        super().__init__(driver)
        self.default_pw = 'Password'

    def click_sign_in(self):
        self.click(*self.CONTINUE_BUTTON)

    def input_credentials(self):
        self.input_text('dyak.ilya@gmail.com', *self.REELLY_EMAIL)
        self.input_text('XrvzakG!E4i@Zzh', *self.REELLY_PASSWORD)

    def click_on_settings(self):
        self.click(*self.CLICK_SETTINGS)

    def edit_profile(self):
        self.click(*self.CLICK_EDIT_PROFILE)

    def input_fields(self):
        self.input_text('Hebrew, Russian', *self.INPUT_FIELD)

    def click_on_save(self):
        self.click(*self.CLICK_SAVE)

