# Main class
import time
from selenium import webdriver

from navigation.common_navigation import CommonNavigation

def main():
    nav = CommonNavigation("https://github.com/")
    driver = nav.get_driver()
    nav.change_url(driver, "https://www.amazon.com/")
    nav.exit_browser(driver)

if __name__ == "__main__":
    main()
