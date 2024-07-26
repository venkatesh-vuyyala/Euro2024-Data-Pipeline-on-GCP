import requests
import csv

url = "https://euro-20242.p.rapidapi.com/players/topScorers"
headers = {
    "x-rapidapi-key": "fce37add80msh0e8ef765a82b793p11823cjsn6b070594c1d9",
    "x-rapidapi-host": "euro-20242.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()  # Extract the JSON data
    csv_filename = 'Topscorer.csv'

    if data:
        field_names = ['goals', 'name', 'teamName', 'assists', 'firstTeamAppearances']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()  # Write the header

            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})

        print(f"Data fetched successfully and written to '{csv_filename}'")
    else:
        print("No data available from the API.")
else:
    print("Failed to fetch data:", response.status_code)
