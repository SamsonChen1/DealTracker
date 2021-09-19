from selenium import webdriver

class CommonNavigation:
    def __init__(self, url):
        self.url = url

    def get_driver(self):
        driver = webdriver.Chrome("C:\Drivers\chromedriver_v93.exe")
        driver.set_window_size(1600, 900)
        driver.get(self.url)
        return driver
