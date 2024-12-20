# Data Scraping Assignment
This repository contains two Python scripts for data scraping as part of a classwork assignment. Each script focuses on extracting specific information from popular websites and saving the processed data into CSV files for further analysis.
## Files and Functionality
### 1. `Classwork_Data_Scrapping_imdb_movie_cast.py`
#### **Description**
This script scrapes data from the IMDb Top 250 movies page to extract the top 200 movies' titles along with their cast information. It generates a CSV file with the rank, title, and main cast of each movie.
#### **Functionality**
- Fetches the IMDb Top 250 movies page using the `requests` library.
- Parses the HTML content with `BeautifulSoup` to locate the JSON data containing the movie list.
- Extracts titles and navigates to individual movie pages to scrape cast information.
- Saves the extracted data into a CSV file named `imdb_top_250_titles_with_cast.csv`.
#### **Modules Used**
- `requests`: For sending HTTP requests to fetch webpages.
- `bs4 (BeautifulSoup)`: For parsing and navigating HTML content.
- `json`: For processing JSON data embedded in the IMDb page.
- `csv`: For writing the extracted data into a CSV file.
---
### 2. `Classwork_Data_Scrapping_wikipedia.py`
#### **Description**
This script scrapes data from the Wikipedia page that lists U.S. states and territories, extracting the state names and their respective populations. It generates a CSV file with the state and population data.
#### **Functionality**
- Fetches the Wikipedia page using the `requests` library.
- Parses the HTML content with `BeautifulSoup` to locate the table containing state and population data.
- Extracts the state abbreviation and dynamically identifies the population column.
- Saves the extracted data into a CSV file named `state_population.csv`.
#### **Modules Used**
- `requests`: For sending HTTP requests to fetch webpages.
- `bs4 (BeautifulSoup)`: For parsing and navigating HTML content.
- `csv`: For writing the extracted data into a CSV file.
---
## Outputs
### Generated CSV Files
1. **`imdb_top_250_titles_with_cast.csv`**
   - Contains the following columns:
     - `Rank`: Rank of the movie in the Top 250 list.
     - `Title`: Title of the movie.
     - `Cast`: Main cast members of the movie.
2. **`state_population.csv`**
   - Contains the following columns:
     - `State`: Abbreviation of the U.S. state or territory.
     - `Population`: Population of the state/territory.
---
## How to Run
1. Install the required Python modules using:
   ```bash
   pip install requests beautifulsoup4
