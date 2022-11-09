from selenium import webdriver
from selenium.webdriver.common.by import By
import time

## Scraper Class that will contain all the methods
class Scraper():

## Opening an incognito browser window and navigates to the URL
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options = options)
        self.tv_show_links = []
    
    def search(self):
        URL = "https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular?page=1"
        self.driver.get(URL)
        time.sleep(5)

## Finds netflix, prime and disney buttons and clicks them (3 most popular/fav streaming)
    def select_streaming_sites(self):
        netflix_button = self.driver.find_element(By.XPATH, '//where-to-watch-bubble[@value="netflix"]')
        netflix_button.click()
        prime_button = self.driver.find_element(By.XPATH, '//where-to-watch-bubble[@value="amazon_prime"]')
        prime_button.click()
        disney_button = self.driver.find_element(By.XPATH, '//where-to-watch-bubble[@value="disney_plus"]')
        disney_button.click()

## Sets Audience Score to Fresh - 60% of reviews are positive
    def high_tomatometer(self):
        sort_by_menu = self.driver.find_element(By.XPATH, '//*[@id="main-page-content"]/div/div[2]/div/filter-chip[1]')
        sort_by_menu.click()
        tomatometer_high_button = self.driver.find_element(By.XPATH, '//select-radio[@value="critic_highest"]')
        tomatometer_high_button.click()


## Selects top 10 shows and collects their links in a list
    def tv_show_links(self):
        tv_show = self.driver.find_elements(By.XPATH, '//a[@class="js-tile-link"]') ## Selects the movie from the list
        for i in range(len(tv_show)):
            self.tv_show_links.append(tv_show[i].get_attribute('href'))
            self.tv_show_links[:10]
            print(self.tv_show_links)


if __name__ == "__main__":
    webscraper = Scraper()
    webscraper.search()
    webscraper.select_streaming_sites()
    webscraper.high_tomatometer()
    webscraper.tv_show_links()
