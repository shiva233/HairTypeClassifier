
# Hair Type Image Scraper

This script uses the `GoogleImagesSearch` library to scrape images of various hair types from Google Images. It is designed to download images based on a list of hair types and save them in specific directories.

## Features

- **Scrapes Images**: Downloads images from Google Images for specified hair types.
- **Retry Mechanism**: Implements a simple retry mechanism to handle potential errors during the search and download process.
- **Organized Storage**: Saves images in directories named after the hair type query.

## Installation

### Prerequisites

- Python 3.x
- An active internet connection
- Google API Key and Custom Search Engine ID (CX)

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/HairTypeClassifier.git
   cd HairTypeClassifier
   ```

2. **Install Dependencies:**

   ```bash
   pip install google-images-search
   ```

3. **Set Up Google Custom Search API:**

   To use the Google Image Scraper, you need to set up a Google Custom Search API and obtain a Search Engine ID (CX) and an API key. Follow these steps:

   #### a. Create a Custom Search Engine

   1. Go to the [Google Custom Search Engine](https://cse.google.com/cse/) website.
   2. Click on "Add" to create a new search engine.
   3. Under "Sites to search," enter any URL (e.g., `www.example.com`). This setting can be adjusted later if needed.
   4. Click "Create."

   #### b. Get the Search Engine ID (CX)

   1. After creating the search engine, go to the "Control Panel" for your search engine.
   2. Copy the Search Engine ID (CX) from the top of the page.

   #### c. Enable the Custom Search API

   1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
   2. Create a new project or select an existing one.
   3. Navigate to "APIs & Services" > "Library."
   4. Search for "Custom Search API" and enable it.

   #### d. Get the API Key

   1. In the Google Cloud Console, go to "APIs & Services" > "Credentials."
   2. Click "Create credentials" and select "API key."
   3. Copy the generated API key.

4. **Configure API Key and CX**

   In the script, replace the placeholders with your actual API key and CX:

   ```python
   api_key = 'your_api_key'
   cx_id = 'your_cx'
   ```

   Replace `your_api_key` and `your_cx` with the API key and CX you obtained earlier.

## Usage

To use the Google Image Scraper, run the script:

```bash
python image_scraper.py
```

The images will be saved in directories named after the hair type (e.g., `1a_hair`, `2b_hair`).

## Code Explanation

```python
from google_images_search import GoogleImagesSearch
from googleapiclient.errors import HttpError
import time
import os

# Replace 'your_api_key' and 'your_cx' with your actual credentials
api_key = 'your_api_key'
cx_id = 'your_cx'
hair_types = ['1a hair', '1b hair', ...]

# Create an instance of GoogleImagesSearch with your API key and CX ID
gis = GoogleImagesSearch(api_key, cx_id)

for hair_type in hair_types:
    max_retries = 3
    retry_count = 0
    success = False

    destination_dir = 'path_to_save_images/{}'.format(hair_type.replace(" ", "_"))
    os.makedirs(destination_dir, exist_ok=True)

    search_params = {
        'q': hair_type,
        'num': 400,
        'safe': 'high',
        'fileType': 'jpg',
        'imgType': 'photo',
        'imgSize': 'medium',
    }

    while retry_count < max_retries and not success:
        try:
            gis.search(search_params=search_params)
            success = True

            for image in gis.results():
                image.download(destination_dir)

        except HttpError as e:
            print(f"An error occurred: {e}")
            retry_count += 1
            if retry_count < max_retries:
                print("Retrying...")
                time.sleep(2)

if not success:
    print("Failed to fetch images after multiple attempts.")
```

### Parameters:

- **`api_key`**: Your Google API key.
- **`cx_id`**: Your Custom Search Engine ID.
- **`hair_types`**: List of hair types to search for.
- **`max_retries`**: Maximum number of retry attempts in case of errors.
- **`destination_dir`**: Directory path where images will be saved.

### Error Handling

The script includes a retry mechanism that attempts to handle `HttpError` exceptions by retrying the request up to a specified number of times (`max_retries`). If all attempts fail, an error message is printed.

## Ethical Considerations

Please use this script responsibly. Ensure that you comply with Google's usage policies and respect copyright laws when collecting and using images.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

Special thanks to the contributors and the open-source community for providing the tools and resources used in this project.
