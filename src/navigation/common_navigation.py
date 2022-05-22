from selenium import webdriver

class CommonNavigation:
    def __init__(self, url):
        self.url = url

    def get_driver(self):
        driver = webdriver.Chrome("C:\Driver\chromedriver.exe")
        driver.set_window_size(1600, 900)
        driver.get(self.url)
        return driver

    def change_url(self, driver, new_url):
        self.url = new_url
        driver.get(self.url)
        return driver

    def exit_browser(self, driver):
        driver.quit()


