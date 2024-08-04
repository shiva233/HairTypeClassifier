# Hair Type Classifier

Hey there! This project is all about classifying hair types. The big dream is to sort hair by specific types from 1a to 4c, but for now, we're keeping it simple with just three main types: Curly, Straight, and Wavy.

## Why We Made This

Finding hairstyles that work for my hair type has always been a struggle. Which is when I had the idea to make something to help others who face the same problem. So, here we are, with this hair-type classifier!

## Getting Started

### Clone the Repo

First things first, grab the code:
```bash
git clone https://github.com/USERNAME/REPO_NAME.git    
```

## Set Up Your Environment
Go to the project directory:
```bash
cd HairTypeClassifier
```
Set up a virtual environment and activate it:
```bash
python -m venv .venv
.\.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux
```

install all the stuff you need:
```bash
pip install numpy opencv-python scikit-learn tensorflow kaggle 
```

## Dataset

### OPTION 1: Making your own dataset:
This option uses web scraping to generate a dataset of images from hair-types 1a-4c. Naturally, you will need to edit the train_model.py and predict_hair_type.py to support 1a-4c instead of curly, wavy and straight. *Instructions on editing the two Python files will be added to a future commit.*

Find documentation for making your own dataset [here](Image-Scraper-Instructions.md).

### OPTION 2: Using an existing dataset from Kaggle:
To use this option before you can train the model, you need to download the dataset from Kaggle. We've provided a script to do this automatically

### Steps
1. Set Up Kaggle API: Make sure you have your Kaggle API key. You can get it from your Kaggle account settings.
2. Make a .Kaggle in C:\Users\YOURNAME and put the .json file/ Kaggle API Key in that folder
3. Download the Dataset: Run the downloadDataset.py script to download and unzip the dataset. (MAKE SURE TO CHANGE FILE PATHS)

```bash
python downloadDataset.py
```
This will download the dataset into the 'data/' directory.

## How to Use It
### Train the Model
To train the mode, just run:
```bash
python train_model.py
```

This will load the dataset, do some magic with the images, train the model, and save it as hair_classification_model.keras.

## Predict Hair Type
To predict the hair type of a new image, edit the predict_hair_type.py to the location of the image you want to predict and then run the predict_hair_type.py.

```bash
python predict_hair_type.py
```

## What's Next and Personal Thoughts

- As we said at the start, this project was originally aimed to sort hair by more specific types such as 1a-4c. Right now we wanted to start with the basics. 
- Future versions will get more detailed, cover all hair types and hopefully be more accurate :)
- We might even add a front end to the project so stay tuned :D

## License
This project is under the MIT License. Check the LICENSE file for more info.

   
