FROM python:3.8

WORKDIR /app

COPY . /app

#Installing requirements from txt file
RUN pip freeze > requirements.txt

COPY requirements.txt requirements.txt

RUN apt-get update

RUN pip install -r requirements.txt

RUN apt-get install -y gnupg \
        wget \
        curl 
        
#Installing Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get -y update

RUN apt-get install -y google-chrome-stable

#Installing Chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

RUN apt-get install -yqq unzip

RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

CMD ["python", "Rotten_Tomatoes_Scraper.py"]