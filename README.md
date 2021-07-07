# nsfw-detection
A python flask api that given an image will return a score on how much it's suitable for work, detecting nudity, violence and drugs.
- For detecting nudity I used [nudeNet](https://github.com/notAI-tech/NudeNet) from notAI
- For violence and drugs detection, I hypertuned mobilenet on my own collected dataset:

## DataSet for violence and drugs
- At first I didn't find any avilable dataset online so I collected I set of Imgs by myself:
  1. **Source of the data:** from google Imgs, duckduckgo Imgs and some from Bing.
  1. **For batch downloading:** I used [Image Downloader](https://chrome.google.com/webstore/detail/image-downloader/cnpniohnfphhjihaiiggeabnkjhpaldj) chrome extension for downloading a bunch of Imgs at once 
  1. **Number of collected Imgs:** The Imgs I've collected With about 1000 Imgs for each class.
  1. **As a third class (Natural):** I used a set of natural Imgs from this [dataSet](https://www.kaggle.com/prasunroy/natural-images) in kaggle make sure to look at the Acknowledgements section In kaggle for this dataset. 
  1. I used Pillow for loading rgb and resizing the Imgs (224, 224) as Imgs size.
  1. Then I augmented the data using the `ImageDataGenerator` Provided by keras.
- For more Detailed Info look at the [data-augmentation](./data_preprocessing/data-augmentation.ipynb) notebook. 

## Installation Instructions
1. Install python3 
2. Install pip3 `$ sudo apt install python3-pip`
3. Install virtualenv `$ python3 -m pip install --user virtualenv`
4. Append virtualenv path to your `$PATH varibale`
    - find out where virtualenv installed `$ which virtualenv`
    - append the output of the above command to `$ export PATH=/the/output/path:$PATH`
5. Create the virtualenv `$ virtualenv --python=$(which python3) venv`
    - Make sure you are in the project folder.
6. Activate virtualenv `$ source venv/bin/activate`
7. Install requirments `$ pip3 install -r requirments.txt`
8. Make sure that the version of pillow lib is Pillow==8.2.0
    - `$ pip freeze | grep Pillow`
    - As there is some lib conflicts with other pillow versions
    - To make sure that everything is okay `$ pip install Pillow==8.2.0`
