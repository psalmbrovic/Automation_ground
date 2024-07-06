
from selenium.webdriver.common.by import By


class LoginLocator:
    USERNAME = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > "
                                 "div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(2) > div "
                                 "> div:nth-child(2) > input")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "submit")


class AdminPageLocator:
    CLICK_ADMIN = (By.XPATH, "//a[normalize-space()='']")
    CLICK_USER_MANAGEMENT = (By.XPATH, "//span[normalize-space()='User Management']//i[@class='oxd-icon bi-chevron-down']")
    CLICK_USERS = (By.XPATH, "//ul[@role='menu']//li")
    CLICK_USERNAME = (By.XPATH, "")
    USER_ROLE = ()
    EMPLOYEE_NAME = ()
    STATUS = ()
    ADMIN = ()
    ESS = ()
    ENABLED = ()
    DISABLED = ()


class Pim:
    PIM = (By.XPATH, "")
    EMPLOYEE_NAME = (By.XPATH, "")
    EMPLOYEE_ID = (By.XPATH, "")
    EMPLOYEE_STATUS_DROPDOWN = (By.XPATH, "")
    FULL_TIME_CONTRACT = (By.XPATH, "")
    INCLUDE_DROPDOWN = (By.XPATH, "")
    CURRENT_PAST_EMPLOYEE = (By.XPATH, "")
    SUPERVISOR_NAME = (By.XPATH, "")
    JOB_TITLE_DROPDOWN = (By.XPATH, "")
    ACCOUNT_ASSISTANT = (By.XPATH, "")
    SUB_UNIT_DROPDOWN = (By.XPATH, "")
    ADMINISTRATION = (By.XPATH, "")
    SEARCH_BUTTON = (By.XPATH, "")
