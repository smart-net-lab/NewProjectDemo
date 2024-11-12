from sys import executable

import pytest
from packaging.markers import Environment
from selenium import webdriver
driver = None

def pytest_addoption(parser):    #Run commandline option - To allow custom command to run on specific browser
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--env_name", action="store", default="preprod"
    )


@pytest.fixture(scope="class")
def setUp(request):

    global driver
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()

    Environment_name = request.config.getoption("--env_name")

    if Environment_name == "STAGING":
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif Environment_name == "PREPROD":
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif Environment_name == "PROD":
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()




# capture the image if any test cases are failed
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)