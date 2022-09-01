import time
from selenium import webdriver
import pytest
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.by import By


def save_new_element(element: WebElement):
    print(element.text)



if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='src/chromedriver.exe')
    driver.get('https://www.tase.co.il/en/market_data/index/137/components/securities_data')
    for i in range(1):
        time.sleep(5)
        print(' start of first for ----', i)
        elements: List[WebElement] = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/index-lobby/index-composition/index-market-data/gridview-lib/div/div[2]/div/div/div[2]/table/tbody/tr')
        for element in elements:
            save_new_element(element)
        print('---- END OF PAGE -------', i)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="pageS"]/pagination-template/ul/li[8]/a').click()
