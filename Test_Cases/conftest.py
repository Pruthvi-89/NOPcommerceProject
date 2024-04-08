import pytest
from  selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")

    elif browser == "Firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")


    elif browser == "Edge":
        driver = webdriver.Edge()
        print("Launching Edge Browser")

    else:
        Chrome_Options = webdriver.ChromeOptions()
        Chrome_Options.add_argument("headless")
        driver= webdriver.Chrome(options=Chrome_Options)

    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    return driver




# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome()
#     # driver.get("https://admin-demo.nopcommerce.com/")
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield driver
#     return driver


@pytest.fixture(params=[
    ("admin@yourstore.com","admin","Pass"),
    ("admin@12yourstore.com","admin","Fail"),
    ("admin@yourstore.com","admin12","Fail"),
    ("admin@13yourstore.com","admin123","Fail")
])
def getDataforLogin(request):
    return request.param



def pytest_metadata(metadata):
    metadata["Environment"]="Test"
    metadata["Project Name"]="NOPcommerce"
    metadata["Modul Name"] = "Employee"
    metadata["Tester"]="Pruthviraj"
    #Remove
    metadata.pop("Packages",None)
    metadata.pop("Plugins",None)
    metadata.pop("Platform",None)



