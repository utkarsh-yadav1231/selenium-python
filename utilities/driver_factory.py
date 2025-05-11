# utilities/driver_factory.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser.lower() == "chrome":
            service = Service(r"C:\chromedriver\chromedriver.exe")
            driver = webdriver.Chrome(service=service)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        # Add more browsers as needed
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
