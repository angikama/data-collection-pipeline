from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import requests
import os
import json
import shutil

from Rotten_Tomatoes_Scraper import Scraper

class ScraperTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.rottentomatoes.com/tv/the_bastard_son_and_the_devil_himself")
        self.test_tv_show_info = {
            "show_name": "THE BASTARD SON & THE DEVIL HIMSELF (2022 - PRESENT)",
            "tv_poster_img": "https://resizing.flixster.com/-uwHJChyI67R3BULWHPfJnB3vF4=/206x305/v2/https://resizing.flixster.com/sRGHxwhazQq0siGh7si2FhE9DOM=/ems.cHJkLWVtcy1hc3NldHMvdHZzZXJpZXMvNWExMDg3ODMtMWM0Yy00NWZjLWIyYzgtZDAzODdlNjMzZDAwLmpwZw==",
         }
        self.filename = "test_filename"
        self.test_path = "test/test_raw_data"


    # tests if the scraper navigates to the page and extracts the right title 
    def test_search(self):
        page_title = self.driver.find_element(By.XPATH, '//*[@id="seriesHeader"]').text
        self.assertEqual("THE BASTARD SON & THE DEVIL HIMSELF (2022 - PRESENT)", page_title)
        print("The correct page title was found")

    def creating_test_folder(self):
        if not os.path.exists(self.test_path):
            os.makedirs(self.test_path)

        self.assertTrue(os.path.exists(self.test_path))
        print("The folder test_raw_data exists.")

    def creating_test_tv_show_folder(self):
        if not os.path.exists(f'test/test_raw_data/{self.filename}'):
            os.makedirs(f'test/test_raw_data/{self.filename}')

        self.assertTrue(os.path.exists(self.test_path/{self.filename}))
        print("The folder for the tv show exists.")

    def writing_test_json(self):
        with open(f'test/test_raw_data/{self.filename}/test_data.json', 'w') as test_output:
            json.dump(self.test_tv_show_info, test_output)

        self.assertTrue(os.path.exists(self.test_path/{self.filename}/self.test_data.json))
        print("The json file exists.")

    def test_saving_image(self):
        test_image_url = self.test_tv_show_info["tv_poster_img"]
        res = requests.get(test_image_url, stream = True)
        image_file_name = "test_image.jpg"
        
        if not os.path.exists(f'test/test_raw_data/{self.filename}/images'):
            os.makedirs(f'test/test_raw_data/{self.filename}/images')
        with open(f'test/test_raw_data/{self.filename}/images/{image_file_name}', 'wb') as f:
            shutil.copyfileobj(res.raw, f)
            
        self.assertTrue(os.path.exists(f'test/test_raw_data/{self.filename}/images/{image_file_name}'))

if __name__ == '__main__':
    unittest.main()
    