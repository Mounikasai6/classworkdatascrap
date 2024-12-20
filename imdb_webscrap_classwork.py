import requests
from bs4 import BeautifulSoup
import json
import csv

# URL of IMDb Top 250 movies
url = "https://www.imdb.com/chart/top"

# Request headers to avoid 403 errors
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Fetch the webpage content
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the JSON data within the <script> tag
    script_tag = soup.find("script", type="application/ld+json")
    
    if script_tag:
        # Load JSON data
        data = json.loads(script_tag.string)
        
        # Extract the list of movies
        movie_list = data.get("itemListElement", [])
        
        # Open a CSV file for writing
        with open("imdb_top_250_titles_with_cast.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            # Write the header
            writer.writerow(["Rank", "Title", "Cast"])
            
            # Loop through the movies and write to the CSV
            for i, movie in enumerate(movie_list[:200], start=1):  # Limit to first 200
                title = movie["item"]["name"]
                movie_url = movie['item']['url']
                
                # Request the individual movie page to scrape the cast
                movie_response = requests.get(movie_url, headers=headers)
                if movie_response.status_code == 200:
                    movie_soup = BeautifulSoup(movie_response.text, "html.parser")
                    
                    # Find the cast list within the page
                    cast_section = movie_soup.find_all(class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
                    cast = [actor.get_text() for actor in cast_section[3:6]]  # Get the first 5 actors
                    
                    # Convert cast list to a comma-separated string
                    cast_str = ", ".join(cast)
                else:
                    cast_str = "Cast not found"
                
                # Write movie data row
                writer.writerow([i, title, cast_str])
        
        print("CSV file 'imdb_top_250_titles_with_cast.csv' created successfully.")
    else:
        print("JSON data not found in the script tag.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")