# Data Collection Pipeline

![image](https://www.rottentomatoes.com/assets/pizza-pie/images/rottentomatoes_logo_40.336d6fe66ff.png)

## A Selenium webscraper containerised using Docker
### Purpose:
- Collects information from the TV show section of the Rotten Tomatoes website
- The user selects:
  - The number of shows to scrape - 5, 10 or 20
  - TV streaming platforms - Netflix, Amazon Prime, Disney+, HBO Max and Apple TV Plus
  - Filters on the shows - A to Z, Most popular, newest, critic's highest and lowest rating, audience's highest and lowest rating
- Application scrapes data including images and saves in JSON files

### Tools used:
- Python
- Selenium
- Docker
- CI/CD pipelines

## Selenium
The Selenium webdriver allows automation of the Google Chrome browser. The methods within the class include:
  - Opening up the browser window and navigating to the website
  - Click the 'Accept cookies' button
  - Click the desired filters
  - Return a list of TV show links
  
  ### Method: Selects the sorting filter
  
  
## Saving data
Data is scraped from each of the links in the list and recorded in a dictionary. Information on each TV show is included, for example, the title, synopsis and genre. The dictionaries holding the data are saved as JSON files in individual folders for each tv show.

  ### Method: Writing the JSON files
  


Using requests and shutil modules, the TV show poster image for each show is downloaded using the url scraped from the individual links and saved in a seperate folder within the original folder for the TV show.

## Testing
To test the scraper, the Unittest module is used. Within the unittest class, the important functions of the scraper are tested, including writing JSON files and downloading the images.

## Containersing using Docker
The application was containerised using Docker. Writing a Dockerfile, allows for the image to install all dependencies needed for the scraper, including ChromeDriver and Google Chrome. The created image can then be run in a container on other machines.

A CI/CD pipeline was also set up for the docker image using GitHub Actions, 'main.yml' contains the workflow that allows for the docker image to be built and pushed. It uses secrets and a Personal Access Token provided by Docker Hub.

## Future additions and ideas for the project
- GUI - user can interact with an interface, better user experience
- Email results to user
