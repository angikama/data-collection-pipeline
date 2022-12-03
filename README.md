# Data Collection Pipeline

![image](https://www.rottentomatoes.com/assets/pizza-pie/images/rottentomatoes_logo_40.336d6fe66ff.png)

This is a webscraper that collects information from the TV show section of the Rotten Tomatoes website. It selects 10 TV shows that are positively reviewed by others, and from 3 subscription sites.

### Tools used
- Selenium
- Docker
- CI/CD pipelines

## Selenium
The Selenium webdriver allows automation of the Google Chrome browser. The methods within the class include:
  - Opening up the browser window and navigating to the website
  - Click the 'Accept cookies' button
  - Click the desired filters - high Tomatometer score, and availiability on 3 streaming sites: Netflix, Disney + and Amazon Prime.
  - Return a list of the first 10 TV show links
  
  Method that selects the 'high tomatometer' filter
  <img width="675" alt="image" src="https://user-images.githubusercontent.com/111760140/205447553-04dece95-389b-40ec-a78b-dbc3324e5b0f.png">

  
## Saving data
Data is scraped from each of the 10 links in the list and recorded in a dictionary. Information on each TV show is included, for example, the title, synopsis and genre. The dictionaries holding the data are saved as JSON files in individual folders for each tv show.

  Method that writes the JSON files
  
  <img width="454" alt="image" src="https://user-images.githubusercontent.com/111760140/205447604-97a10258-b1d5-44d2-b923-1df6c579d37a.png">


Using requests and shutil modules, the TV show poster image for each show is downloaded using the url scraped from the individual links and saved in a seperate folder within the original folder for the TV show.

## Testing
To test the scraper, the Unittest module is used. Within the unittest class, the important functions of the scraper are tested, including writing JSON files and downloading the images.

## Containersing using Docker
The application was containerised using Docker. Writing a Dockerfile, allows for the image to install all dependencies needed for the scraper, including ChromeDriver and Google Chrome. The created image can then be run in a container on other machines.

A CI/CD pipeline was also set up for the docker image using GitHub Actions, 'main.yml' contains the workflow that allows for the docker image to be built and pushed. It uses secrets and a Personal Access Token provided by Docker Hub.
