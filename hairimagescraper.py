from google_images_search import GoogleImagesSearch
from googleapiclient.errors import HttpError
import time
import os

# Replace 'your_api_key' and 'your_cx' with your actual credentials
api_key = 'YOUR API KEY'
cx_id = 'YOUR CX ID'
hair_types = ['1a hair', '1b hair', '1c hair', '2a hair', '2b hair', '2c hair', '3a hair', '3b hair', '3c hair', '4a hair', '4b hair', '4c hair']

# Create an instance of GoogleImagesSearch with your API key and CX ID
gis = GoogleImagesSearch(api_key, cx_id)

for hair_type in hair_types:
    # Define a simple retry mechanism
    max_retries = 3
    retry_count = 0
    success = False

    # Set the destination directory 
    destination_dir = 'D:\\Apps\\Programing\\Python\\imagescraper\\hairimages\\{}'.format(hair_type.replace(" ", "_"))

    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Define search parameters for specific queries, using the hair_types as the query
    search_params = {
        'q': hair_type,
        'num': 5,
        'safe': 'high',
        'fileType': 'jpg',
        'imgType': 'photo',
        'imgSize': 'medium',
    }

    while retry_count < max_retries and not success:
        try:
            # Perform the search
            gis.search(search_params=search_params)
            success = True  # If search succeeds, break out of the loop

            # Download the images to the specified path
            for image in gis.results():
                image.download(destination_dir)

        except HttpError as e:
            print(f"An error occurred: {e}")
            retry_count += 1
            if retry_count < max_retries:
                print("Retrying...")
                time.sleep(2)  # Wait for 2 seconds before retrying

if not success:
    print("Failed to fetch images after multiple attempts.")