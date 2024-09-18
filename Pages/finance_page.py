from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class FinancePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def compare_and_print_stock_symbol(self,data):
        css_selector_for_stock_symbol = (
            "#yDmH0d > c-wiz.zQTmif.SSPGKf.ccEnac > div > div.e1AOyf > div > div > div.fAThCb > "
            "c-wiz:nth-child(1) > div > section > ul > li > a > div > div > div.iLEcy >"
            " div.rzR5Id > div > div")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector_for_stock_symbol))
        )
        stock_symbol = self.driver.find_elements(By.CSS_SELECTOR,
                                            css_selector_for_stock_symbol)
        # Compare and print stock symbol
        print("\n")
        stock_symbol_from_site = []
        for i in stock_symbol:
            stock_symbol_from_site.append(i.text)
        # Print all stock symbols that are on the site  but not in given test data
        for i in stock_symbol_from_site:
            if i not in data:
                print(i, end=',')
        print("\n")

        # Print all stock symbols that are in given test data  but not on site
        for i in data:
            if i not in stock_symbol_from_site:
                print(i, end=',')
        print("\n")