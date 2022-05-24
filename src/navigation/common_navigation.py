from selenium import webdriver
from bs4 import BeautifulSoup

class CommonNavigation:
    def __init__(self, url):
        self.url = url
        self.driver = self.get_driver()
        self.soup = BeautifulSoup(self.driver.page_source, "html.parser")

    def get_driver(self):
        driver = webdriver.Chrome("C:\Driver\chromedriver.exe")
        driver.set_window_size(1600, 900)
        driver.get(self.url)
        return driver

    def change_url(self,  new_url):
        self.url = new_url
        self.driver.get(self.url)
        return self.driver

    def exit_browser(self):
        self.driver.quit()

