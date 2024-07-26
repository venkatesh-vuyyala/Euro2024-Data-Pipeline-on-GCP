import requests
import csv
from google.cloud import storage



url = "https://euro-20242.p.rapidapi.com/players/topScorers"
headers = {
    "x-rapidapi-key": "fce37add80msh0e8ef765a82b793p11823cjsn6b070594c1d9",
    "x-rapidapi-host": "euro-20242.p.rapidapi.com"
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()  
    csv_filename = 'Topscorer.csv'

    if data:
        field_names = ['goals', 'name', 'teamName', 'assists', 'firstTeamAppearances']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            # writer.writeheader()
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})

        print(f"Data fetched successfully and written to '{csv_filename}'")

        # Upload the CSV file to GCS
        bucket_name = 'player_ranking_data'
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}'  # The path to store in GCP

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
    else:
        print("No data available from the API.")
else:
    print("Failed to fetch data:", response.status_code)