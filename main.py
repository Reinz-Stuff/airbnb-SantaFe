import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

URL = 'https://www.airbnb.com/s/experiences?tab_id=experience_tab&refinement_paths%5B%5D=%2Fexperiences' \
      '&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&source' \
      '=structured_search_input_header&search_type=user_map_move&place_id=ChIJP_ixMuBFGIcR4E56nJe0kuE&rank_mode' \
      '=default&kg_or_tags%5B%5D=Tag%3A2513&ne_lat=71.42652271989226&ne_lng=-61.64770738800678&sw_lat=23' \
      '.70395117140717&sw_lng=-152.70239488800678&zoom=4&search_by_map=true '

driver = webdriver.Chrome('C:/chromedriver.exe')

driver.get(URL)

contents = driver.find_elements(By.CSS_SELECTOR, "div:nth-child(3) > div > div > div > div > div > div > div > div > div > div > div > div.cpzcz7c.dir.dir-ltr > a")
airbnb = 'https://www.airbnb.com'

data = []
for content in contents:
    link = airbnb + content.get_dom_attribute('href')
    data_dict = {
        'Link': link
    }
    data.append(data_dict)

try:
    os.mkdir('results')
except FileExistsError:
    pass
df = pd.DataFrame(data)
df.to_csv(f'results/result.csv', index=False)
df.to_excel(f'results/result.xlsx', index=False)
df.to_json(f'results/result.json', orient='records')

