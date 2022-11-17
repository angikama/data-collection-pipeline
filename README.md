# Data Collection Pipeline

I have selected the TV show section of the Rotten Tomatoes website because I enjoy watching TV series in my spare time. I do prefer to watch ones that are positively reviewed by others, and I would like a way to search shows from subscriptions I have all at once.

The scraper selects 10 TV shows that have been filtered by high Tomatometer score, and availiability on 3 streaming sites: Netflix, Disney + and Amazon Prime.

The Selenium webdriver allows automation of the Google Chrome browser, the methods within the class open up the browser window and naviagte to the website. They also allow the desired filters to be selected to return a list of 10 TV show links.

Data is scraped from each link in the list and recorded in a dictionary. Information on each TV show is included, for example, the title, synopsis and genre. The dictionaries holding the data are saved as JSON files in individual folders for each tv show.

Using requests and shutil modules, the TV show poster image for each show is downloaded using the url scraped from the individual links and saved in a seperate folder within gthe original folder for the TV show.