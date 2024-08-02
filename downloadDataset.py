import os
import zipfile

# Set the Kaggle configuration directory
os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('C:/Users/Shiva/.kaggle')

# Set the destination directory on the D drive
destination_dir = 'D:/Coding Stuff/Dataset'

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Download the dataset using Kaggle API
os.system(f'kaggle datasets download -d vyombhatia/the-three-hair-types -p "{destination_dir}"')

# Unzip the dataset
with zipfile.ZipFile(f'{destination_dir}/the-three-hair-types.zip', 'r') as zip_ref:
    zip_ref.extractall(destination_dir)
