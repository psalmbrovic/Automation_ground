from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from Locator_Page.Locator import LoginLocator, Pim, AdminPageLocator


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def input_username(self, username):
        input_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.USERNAME))
        input_username.send_keys(username)

    def input_password(self, password):
        input_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD))
        input_password.send_keys(password)

    def login(self):
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(LoginLocator.LOGIN))
        login_button.click()


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def click_admin(self):
        click_admin = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminPageLocator.CLICK_ADMIN))
        click_admin.click()
