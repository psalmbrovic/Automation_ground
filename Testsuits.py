import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from Action_page.ActionPage import LoginPage, AdminPage


# @pytest.fixture(scope="module")
# def driver_setup():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#     chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return login_page


def test_login_page_on_orange_website(login):
    login.input_username("Admin")
    login.input_password("admin123")
    login.login()


def test_admin_page_on_orange_website(login):
    test_admin_page = AdminPage(login.driver)
    test_admin_page.click_admin()


