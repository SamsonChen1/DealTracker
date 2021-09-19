# Main class
from datetime import time
from selenium import webdriver

from navigation.common_navigation import CommonNavigation

def main():
    nav = CommonNavigation("https://github.com/")
    driver = nav.get_driver()
    driver.exit()

if __name__ == "__main__":
    main()
