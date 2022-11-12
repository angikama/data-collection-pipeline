from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
dt = datetime.now()


## Scraper Class that will contain all the methods
class Scraper():

## Opening an incognito browser window and navigates to the URL
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        # options.headless = True        Add in when code is complete 
        self.driver = webdriver.Chrome(options = options)
        self.tv_show_links = []
    
    def search(self):
        URL = "https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular?page=1"
        self.driver.get(URL)
        time.sleep(5)

## Sets high tomatometer filter
    def high_tomatometer(self):
        sort_by_menu = self.driver.find_element(By.XPATH, '//*[@id="main-page-content"]/div/div[2]/div/filter-chip[1]')
        sort_by_menu.click()
        tomatometer_high_button = self.driver.find_element(By.XPATH, '//select-radio[@value="critic_highest"]')
        tomatometer_high_button.click()
        time.sleep(5)

## Finds netflix, prime and disney buttons and clicks them (3 most popular/fav streaming)
    def select_streaming_sites(self):
        netflix_button = self.driver.find_element(By.XPATH, '//where-to-watch-bubble[@value="netflix"]')
        netflix_button.click()
        prime_button = self.driver.find_element(By.XPATH, '//where-to-watch-bubble[@value="amazon_prime"]')
        prime_button.click()
        disney_button = self.driver.find_element(By.XPATH, '//where-to-watch-bubble[@value="disney_plus"]')
        disney_button.click()
        time.sleep(10)

## Selects top 10 shows and collects their links in a list
    def top_tv_links(self):
        tv_shows = self.driver.find_elements(By.XPATH, '//a[@class="js-tile-link"]') ## Selects the movie from the list
        for i in range(len(tv_shows)):
            self.tv_show_links.append(tv_shows[i].get_attribute('href'))
            self.tv_show_links[:10]
        time.sleep(5)   

## Retriving text and image data from the individual links and adding to dictionary
    def tv_show_data(self):
        tv_show_info = {}
        for i in range(len(self.tv_show_links)):
            show = self.tv_show_links[i]
            self.driver.get(show)
            self.show_name = self.driver.find_element(By.XPATH, '//*[@id="seriesHeader"]')
            self.tv_poster_img = self.driver.find_element(By.XPATH, '//img[@class="posterImage"]')
            self.synopsis = self.driver.find_element(By.XPATH, '//*[@id="movieSynopsis"]')
            self.tv_network = self.driver.find_element(By.XPATH, '//*[@id="detail_panel"]/div/table/tbody/tr[1]/td[2]')
            self.genre = self.driver.find_element(By.XPATH, '//*[@id="detail_panel"]/div/table/tbody/tr[3]/td[2]')
            self.avg_tomatometer_score = self.driver.find_element(By.XPATH, '//*[@id="tomato_meter_link"]/span/span[2]')
            self.timestamp = dt
            
            tv_show_info['show_name'] = self.show_name.text
            tv_show_info['tv_poster_img'] = self.tv_poster_img.get_attribute('src')
            tv_show_info['synopsis'] = self.synopsis.text
            tv_show_info['tv_network'] = self.tv_network.text
            tv_show_info['genre'] = self.genre.text,
            tv_show_info['avg_tomatometer_score'] = self.avg_tomatometer_score.text
            tv_show_info['timestamp'] = self.timestamp
            

if __name__ == "__main__":
    webscraper = Scraper()
    webscraper.search()
    webscraper.high_tomatometer()
    webscraper.select_streaming_sites()
    webscraper.top_tv_links()
    webscraper.tv_show_data()
