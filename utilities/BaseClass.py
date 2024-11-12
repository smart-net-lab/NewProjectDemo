import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.homePage import homePage


@pytest.mark.usefixtures("setUp")
class BaseClass:


    def locatorPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


    def selectOptionByText(self, locater, text):
        sel = Select(locater)
        sel.select_by_visible_text(text)


    def getLog(self):
        loggerName =  inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # name is used to catch the  test_file Name during runtime.

        fileHandler = logging.FileHandler('../Reports/logStm.log')  # allocated a file name to capture logs
        formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s :%(message)s")  # Formate to capture in logstm.log file
        fileHandler.setFormatter(formatter)  # Pass the formatted messg to file

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger






