from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
from datetime import datetime

import json
import os
import requests
import shutil


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

    def __init__(self):
        '''
        Class constructor for Scraper object

        '''
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--headless") 
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.tv_show_links = []
        self.tv_show_info = {}
        self.now = datetime.now()
      
    
    def search(self):
        '''
        Searches the link

        Parameters:
        ------------
            self


        '''
        URL = "https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular?page=1"
        self.driver.get(URL)
    
    def accept_cookies(self):
        '''
        Waits for the element to be clickable then clicks the button that accepts cookies

        Parameters:
        ------------
            self
        '''
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()
        except:
            print("Cookies button not clicked")

    def select_streaming_sites(self):
        '''
        Allows user to select streaming services filters and clicks them : Netflix, Amazon Prime, Disney+, HBO Max and Apple TV Plus

        '''
        self.user_choices = ['netflix', 'hulu', 'disney_plus', 'amazon_prime', 'hbo_max', 'apple_tv_plus']
        for choice in self.user_choices:
            try:
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f'//where-to-watch-bubble[@value={choice}]'))).click()
            except:
                print('An invalid streaming service was selected')


    def filters(self):
        '''
        Opens filter menu and selects chosen filter: A to Z, Most popular, newest, critic's highest and lowest rating, audience's highest and lowest rating

        '''
        self.filter_choices = ['critic_lowest', ' critic_highest', 'audience_highest', 'audience_lowest', 'newest', 'popular', 'a_z']
        self.driver.find_element(By.XPATH, '//*[@id="main-page-content"]/div/div[2]/div/filter-chip[1]').click()
        for filter_choice in self.filter_choices:
            try:
                self.driver.find_element(By.XPATH, f'//select-radio[@value={filter_choice}]').click()
            except:
                print('Filters could not be selected')


    def tv_links(self):
        '''
        Collects the links of the first 10 shows on the page

        '''
        for i in range():
            tv_shows = self.driver.find_elements(By.XPATH, '//a[@class="js-tile-link"]')
            url = tv_shows[i].get_attribute('href')
            self.tv_show_links.append(url)
        time.sleep(5)   

    def tv_show_data(self):
        '''
        Retrieves text data from the page and saves them to a dictionary

        '''
        for link in (self.tv_show_links):
            self.driver.get(link)
            self.tv_show_info["show_name"] = self.driver.find_element(By.XPATH, '//*[@id="seriesHeader"]').text
            self.tv_show_info["tv_poster_img"] = self.driver.find_element(By.XPATH, '//img[@class="posterImage"]').get_attribute("src")
            self.tv_show_info["synopsis"] = self.driver.find_element(By.XPATH, '//*[@id="movieSynopsis"]').text
            self.tv_show_info["tv_network"] = self.driver.find_element(By.XPATH, '//*[@id="detail_panel"]/div/table/tbody/tr[1]/td[2]').text
            self.tv_show_info["genre"] = self.driver.find_element(By.XPATH, '//*[@id="detail_panel"]/div/table/tbody/tr[3]/td[2]').text
            self.tv_show_info["avg_tomatometer_score"] = self.driver.find_element(By.XPATH, '//*[@id="tomato_meter_link"]/span/span[2]').text
            self.tv_show_info["timestamp"] = self.now.strftime("%d/%m/%Y, %H:%M:%S")


    def writing_json(self):
        '''
        Saves dictionary as a json file in an individual folder

        '''
        filename = self.tv_show_info["show_name"]
        if not os.path.exists('raw_data'):
            os.makedirs('raw_data')
        if not os.path.exists(f'raw_data/{filename}'):
            os.makedirs(f'raw_data/{filename}')       
        with open(f'raw_data/{filename}/data.json', 'w') as output:
            json.dump(self.tv_show_info, output)
            
    def saving_image(self):
        '''
        Retrieves image from url and downloads them to seperate folder within the corresponding TV show folder

        '''
        image_url = self.tv_show_info["tv_poster_img"]
        timestamp_now = str(self.now)
        image_file_name = timestamp_now+".jpg"
        
        res = requests.get(image_url, stream = True)
        filename = self.tv_show_info["show_name"]
        if not os.path.exists('raw_data'):
            os.makedirs('raw_data')
        if not os.path.exists(f'raw_data/{filename}/images'):
            os.makedirs(f'raw_data/{filename}/images')   
        with open(f'raw_data/{filename}/images/{image_file_name}', 'wb') as f:
            shutil.copyfileobj(res.raw, f)


if __name__ == "__main__":
    webscraper = Scraper()
    webscraper.search()
    webscraper.select_streaming_sites()
    webscraper.filters()
    webscraper.tv_links()
    webscraper.tv_show_data()
    webscraper.writing_json()
    webscraper.saving_image()  
