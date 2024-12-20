import requests
from bs4 import BeautifulSoup
import csv

# URL of the Wikipedia page for U.S. states and territories
url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"

# Fetch the webpage content
response = requests.get(url)
a = response.content
soup = BeautifulSoup(a, 'html.parser')

# Locate the table containing the state and population data
table = soup.find(class_='wikitable sortable mw-datatable sticky-header-multi sort-under plainrowheaders')
if table:
    # Extract all rows of the table
    rows = table.find_all('tr')

    # Prepare to store state and population data
    data = []

    # Process each row
    for row in rows[2:]:  # Skip header rows
        cells = row.find_all('td')
        if len(cells) >= 4:  # Ensure there are enough cells in the row
            # Extract the state abbreviation (first column)
            state_abbr = cells[0].text.strip()
            
            # Dynamically identify the population column
            population = None
            for cell in cells:
                div = cell.find('div')
                # Check if the <div> contains numeric text (population)
                if div and div.text.strip().replace(',', '').isdigit():
                    population = div.text.strip()
                    break
            
            # Add data to the list if both state and population are found
            if state_abbr and population:
                data.append((state_abbr, population))

    # Write the extracted data into a CSV file
    with open('state_population.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header row
        csvwriter.writerow(['State', 'Population'])
        # Write the state and population data
        csvwriter.writerows(data)

    # Print the state and population data
    print("State and Population:")
    for state, population in data:
        print(f"{state}: {population}")

else:
    print("Table not found!")