from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FinancePage:
    def __init__(self, driver):
        self.driver = driver


    def open_page(self, url):
        self.driver.get(url)

    def compare_and_print_stock_symbol(self, data, stock_symbol):
        print("\n")
        stock_symbol_from_site = []
        for i in stock_symbol:
            stock_symbol_from_site.append(i.text)

        for i in stock_symbol_from_site:
            if i not in data:
                print(i, end=',')
        print("\n")
        for i in data:
            if i not in stock_symbol_from_site:
                print(i, end=',')