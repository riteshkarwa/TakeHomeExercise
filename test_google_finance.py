import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("data", [["NFLX","MSFT", "TSLA"]])
def test_google_finance(data):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=option)
    driver.get("https://www.google.com/finance/")
    assert "Google Finance - Stock Market Prices, Real-time Quotes & Business News" == driver.title
    css_selector_for_stock_symbol = ("#yDmH0d > c-wiz.zQTmif.SSPGKf.ccEnac > div > div.e1AOyf > div > div > div.fAThCb > "
                                     "c-wiz:nth-child(1) > div > section > ul > li > a > div > div > div.iLEcy >"
                                     " div.rzR5Id > div > div")
    element = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.CSS_SELECTOR, css_selector_for_stock_symbol))
          )
    stock_symbol = driver.find_elements(By.CSS_SELECTOR,
                                        css_selector_for_stock_symbol)
    print("\n")
    stock_symbol_from_site = []
    for i in stock_symbol:
        stock_symbol_from_site.append(i.text)

    for i in stock_symbol_from_site:
        if i not in data:
            print(i,end=',')
    print("\n")
    for i in data:
        if i not in stock_symbol_from_site:
            print(i,end=',')
    driver.close()
    driver.quit()