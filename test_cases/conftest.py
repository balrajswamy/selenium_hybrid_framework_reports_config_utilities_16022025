import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser: chrome or edge or firefox")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver

    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif (browser == "edge"):
        driver = webdriver.Edge()
        driver.maximize_window()
    elif (browser == "firefox"):
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        raise ValueError("Unsupported browser")

    return driver

def pytest_configure(config):
    config.stash[metadata_key]["Project Name"]= "Admin Login OpenCart"
    config.stash[metadata_key]["Test Module Name"] = "Admin Login Test"
    config.stash[metadata_key]["Tester Name"] = "Balraj"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)
