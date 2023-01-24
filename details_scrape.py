import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with open('results/result.json') as json_file:
    datas = json.load(json_file)


def details_scrape():
    driver = webdriver.Chrome('C:/chromedriver.exe')
    url = "https://www.airbnb.com/experiences/132375?currentTab=experience_tab&federatedSearchId=e74343bc-d4f2-44b5-bcbb-261b1bd0e7d3&searchId=b06b2908-16d1-40ae-a1bb-0864f164d27b&sectionId=7f116f53-1a8d-42d9-a67a-0055d302498a"
    driver.get(url)
    driver.maximize_window()

    # time.sleep(10)

    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div > div > div > section > div > div._b8stb0 > span._1qk2y0c > h1')))
    host = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(3) > div > div._16e70jgn > div > div:nth-child(1) > div > div > section > div > div:nth-child(1) > div.t1d2nv5w.dir.dir-ltr > h2')

    # about_button = driver.find_element(By.XPATH, '//*[@id="site-content"]/div[1]/div[3]/div/div[1]/div/div[3]/div/div[2]/span/div[2]/div/button')
    # about_button.click()
    about_host = driver.find_element(By.CSS_SELECTOR, '#site-content > div:nth-child(1) > div:nth-child(3) > div > div._16e70jgn > div > div:nth-child(3) > div > div:nth-child(2) > span > div > span')

    print(title.text, host.text, about_host.text)


# def result():
#     for data in datas:
#         details_scrape(data['Link'])


if __name__ == '__main__':
    details_scrape()
    # result()

