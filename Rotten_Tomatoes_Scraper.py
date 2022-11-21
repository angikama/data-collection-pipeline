from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from datetime import datetime
now = datetime.now()

import json
import os

import requests
import shutil

## Scraper Class that will contain all the methods
class Scraper():
    '''
    This class represents the Rotten Tomatoes Web Scraper

    Attributes:
    ------------
        None

    Methods:
    ------------
        __init__(self)
    
    '''

## Opening an incognito browser window and navigates to the URL
    def __init__(self):
        '''
        Class constructor for Scraper object

        '''
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        # options.headless = True        Add in when code is complete 
        self.driver = webdriver.Chrome(options = options)
        self.tv_show_links = []
        self.tv_show_info = {}
      
    
    def search(self):
        '''
        Searches the link

        Parameters:
        ------------
            self


        '''
        URL = "https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular?page=1"
        self.driver.get(URL)
        time.sleep(5)

    def select_streaming_sites(self):
        '''
        Selects streaming services filters and clicks them : Netflix, Amazon Prime and Disney+

        Parameters:
        ------------
            self

        '''
        netflix_button = self.driver.find_element(By.XPATH, '//where-to-watch-bubble[@value="netflix"]')
        netflix_button.click()
        prime_button = self.driver.find_element(By.XPATH, '//where-to-watch-bubble[@value="amazon_prime"]')
        prime_button.click()
        disney_button = self.driver.find_element(By.XPATH, '//where-to-watch-bubble[@value="disney_plus"]')
        disney_button.click()
        time.sleep(8)


    def high_tomatometer(self):
        '''
        Opens filter menu and selects High Tomatometer

        Parameters:
        ------------
            self

        '''
        sort_by_menu = self.driver.find_element(By.XPATH, '//*[@id="main-page-content"]/div/div[2]/div/filter-chip[1]')
        sort_by_menu.click()
        tomatometer_high_button = self.driver.find_element(By.XPATH, '//select-radio[@value="critic_highest"]')
        tomatometer_high_button.click()
        time.sleep(5)


    def top_tv_links(self):
        '''
        Collects the links of the first 10 shows on the page

        Parameters:
        ------------
            self

        '''
        for i in range(10):
            tv_shows = self.driver.find_elements(By.XPATH, '//a[@class="js-tile-link"]')
            url = tv_shows[i].get_attribute('href')
            self.tv_show_links.append(url)
        time.sleep(5)   

    def tv_show_data(self):
        '''
        Retrieves text data from the page and saves them to a dictionary

        Parameters:
        ------------
            self

        '''
        for link in range(len(self.tv_show_links)):
            show = self.tv_show_links[link]
            self.driver.get(show)
            self.show_name = self.driver.find_element(By.XPATH, '//*[@id="seriesHeader"]')
            self.tv_poster_img = self.driver.find_element(By.XPATH, '//img[@class="posterImage"]')
            self.synopsis = self.driver.find_element(By.XPATH, '//*[@id="movieSynopsis"]')
            self.tv_network = self.driver.find_element(By.XPATH, '//*[@id="detail_panel"]/div/table/tbody/tr[1]/td[2]')
            self.genre = self.driver.find_element(By.XPATH, '//*[@id="detail_panel"]/div/table/tbody/tr[3]/td[2]')
            self.avg_tomatometer_score = self.driver.find_element(By.XPATH, '//*[@id="tomato_meter_link"]/span/span[2]')
            
            self.tv_show_info["show_name"] = self.show_name.text
            self.tv_show_info["tv_poster_img"] = self.tv_poster_img.get_attribute("src")
            self.tv_show_info["synopsis"] = self.synopsis.text
            self.tv_show_info["tv_network"] = self.tv_network.text
            self.tv_show_info["genre"] = self.genre.text
            self.tv_show_info["avg_tomatometer_score"] = self.avg_tomatometer_score.text
            self.tv_show_info["timestamp"] = now.strftime("%d/%m/%Y, %H:%M:%S")

            filename = self.tv_show_info["show_name"]

            def writing_json():
                '''
                Saves dictionary as a json file in an individual folder

                Parameters:
                ------------
                    None

                '''
                if not os.path.exists('raw_data'):
                    os.makedirs('raw_data')
                if not os.path.exists(f'raw_data/{filename}'):
                    os.makedirs(f'raw_data/{filename}')       
                with open(f'raw_data/{filename}/data.json', 'w') as output:
                    json.dump(self.tv_show_info, output)
            
            def saving_image():
                '''
                Retrieves image from url and downloads them to seperate folder within the corresponding TV show folder

                Parameters:
                ------------
                    None

                '''
                image_url = self.tv_show_info["tv_poster_img"]
                timestamp_now = str(now)
                image_file_name = timestamp_now+".jpg"
                
                res = requests.get(image_url, stream = True)
                # saves image
                if not os.path.exists('raw_data'):
                    os.makedirs('raw_data')
                if not os.path.exists(f'raw_data/{filename}/images'):
                    os.makedirs(f'raw_data/{filename}/images')   
                with open(f'raw_data/{filename}/images/{image_file_name}', 'wb') as f:
                    shutil.copyfileobj(res.raw, f)
        
            writing_json()
            saving_image()
    

if __name__ == "__main__":
    webscraper = Scraper()
    webscraper.search()
    webscraper.select_streaming_sites()
    webscraper.high_tomatometer()
    webscraper.top_tv_links()
    webscraper.tv_show_data()
  
