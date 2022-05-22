# Main class
import time
from selenium import webdriver

from navigation.common_navigation import CommonNavigation
from navigation.home_depot_page import HomeDepotPage

def main():
    # nav = CommonNavigation("https://www.homedepot.com/p/KRAUS-Britt-Single-Handle-Pull-Down-Kitchen-Faucet-with-Dual-Function-Sprayer-in-Brushed-Gold-KPF-1690BG/312203762?")
    nav = CommonNavigation("https://www.homedepot.com/p/Swaner-Hardwood-1-in-x-8-in-x-8-ft-Red-Oak-S4S-Board-2-Pack-OL04070896OR/310806332")
    driver = nav.get_driver()
    product_search = HomeDepotPage(driver)
    product_search.get_curr_price()
    if product_search.is_on_sale():
        print("Product is on SALE!!!!!!!!!!!!")
    else:
        print("Product is not discounted.")
    nav.exit_browser(driver)

if __name__ == "__main__":
    main()
