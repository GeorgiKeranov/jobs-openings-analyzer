# Jobs Openings Analyzer
Automate getting the number of job openings for multiple search terms in big job board sites like LinkedIn and Indeed and then show the web scraped data in a bar chart so you can see which jobs are in demand right at the moment when you run the script

## Table of Contents
- [Technologies used](#technologies-used)
- [Functionalities](#functionalities)
- [Installation](#installation)
- [How to Search](#how-to-search)
- [Examples of Analyzed Data - 11.08.2021](#examples-of-analyzed-data-11082021)

## Technologies Used
- Python
- Selenium
- BeatifulSoup
- Matplotlib
- Pickle

## Functionalities
- You can search with your own search keywords
- You can search by worldwide on-site or remote jobs in these job boards - LinkedIn, Indeed

## Installation
1. You will need to have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed
2. You will need to install the following packages with "pip":
    - Linux commands:
      ```
      pip install selenium
      pip install beautifulsoup4
      pip install matplotlib
      pip install pickle-mixin
      ```
    - Windows commands:
      ```
      python -m pip install selenium
      python -m pip install beautifulsoup4
      python -m pip install matplotlib
      python -m pip install pickle-mixin
      ```

## How to Search
1. Open folder where this project is saved on your local machine
2. Open "jobs_search_terms.txt" and remove all of the terms then add search terms that you want to analyze. Please note that each term need to be on a separate line
3. Open terminal inside the project folder
4. Run main.py with this command:
  ```
  python main.py
  ```
4. The terminal will ask to select an option to search jobs - "on_site", "remote" or "both" so you have to type in the console one of these options and click enter
5. The terminal will ask to select a site from which will be the data taken - "linkedin" or "indeed" so you need to type one of them and click enter
6. (Optional) If you have choosen "remote" or "both" and "linkedin" you will be asked for LinkedIn username and password in the terminal because the remote jobs count can only be scraped from logged in user.

## Examples of Analyzed Data 11.08.2021

![languages-jobs-indeed-11-08-2021](https://user-images.githubusercontent.com/22518317/140796636-25fc9dd0-8034-4d37-b421-708f4646d171.png)
![languages-jobs-linkedin-11-08-2021](https://user-images.githubusercontent.com/22518317/140796666-b3f125c7-f58e-4fcb-9a9c-7fe512452c52.png)
![frameworks-jobs-indeed-11-08-2021](https://user-images.githubusercontent.com/22518317/140796680-1b0edc88-7147-4ffa-bac4-a4b711c976ba.png)
![frameworks-jobs-linkedin-11-08-2021](https://user-images.githubusercontent.com/22518317/140796695-d1cda47e-11c1-4143-a7ed-1e251246ba29.png)
![languages-remote-jobs-indeed-11-08-2021](https://user-images.githubusercontent.com/22518317/140796717-95bc62c6-d890-4dec-a1fc-6bf2bcc5baa7.png)
![languages-remote-jobs-linkedin-11-08-2021](https://user-images.githubusercontent.com/22518317/140796723-f71ecf36-429f-40db-a342-a963cf675185.png)
