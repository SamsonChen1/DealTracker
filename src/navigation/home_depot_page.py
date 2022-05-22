from selenium import webdriver
from bs4 import BeautifulSoup

from navigation.common_navigation import CommonNavigation

class HomeDepotPage(CommonNavigation):
    def __init__(self, driver):
        self.soup = BeautifulSoup(driver.page_source, "html.parser")

    def get_curr_price(self):
        price_element = self.soup.find(class_="price-format__large price-format__main-price")
        price_list = price_element.find_all("span")
        if len(price_list) == 3:
            print(f"{price_list[0].string}{price_list[1].string}.{price_list[2].string}")
        else:
            print(f"Investigate the html for the price: {price_element}")

    def is_on_sale(self):
        prev_price = self.soup.find(class_="price-detailed__was-price")
        if prev_price:
            return True
        else:
            return False