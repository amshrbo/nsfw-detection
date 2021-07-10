# nsfw-detection
Nudity, violence and drugs detection using [nudeNet](https://github.com/notAI-tech/NudeNet) for nudity, for violence and drugs detection hyper-tuned mobilenet model on my own collected dataset, the final results is a python flask API that takes an image or a set of images, will return a score on how much it's suitable for work.
- For detecting nudity I used [nudeNet](https://github.com/notAI-tech/NudeNet) from notAI
- For violence and drugs detection, **I hypertuned mobilenet** on my own collected dataset:
- The nudity score is from 100% on his own, and the other three classes from 100% (violence, drugs, and natural).
> This project is still **Under development** for more info about the next release look at the [To Do section](#to-do).

## Tables of contents
1. [Describing the DataSet](#dataset-for-violence-and-drugs)
2. [Training the Model](#training-the-model)
3. [Installation instructions](#installation-instructions)
4. [To Do](#to-do).
5. [What did I learn from this project?](#lessons-from-this-project)
6. [Contacts](#contacts-or-for-more-info)
7. [License](#license)

## DataSet for violence and drugs
- At first I didn't find any avilable dataset online so I collected I set of Imgs by myself:
  1. **Source of the data:** from google Imgs, duckduckgo Imgs and some from Bing.
  1. **For batch downloading:** I used [Image Downloader](https://chrome.google.com/webstore/detail/image-downloader/cnpniohnfphhjihaiiggeabnkjhpaldj) chrome extension for downloading a bunch of Imgs at once 
  1. **Number of collected images:** The images I've collected was about 1000 image for each class.
  1. **As a third class (Natural):** I used a set of natural images from this [dataSet](https://www.kaggle.com/prasunroy/natural-images) in kaggle make sure to look at the Acknowledgements section In kaggle for this dataset. 
  1. I used Pillow for loading rgb and resizing the images (224, 224) as images size.
  1. Then I augmented the data using the `ImageDataGenerator` Provided by keras to make every class about 3000 images.
- For more Detailed Info look at the [data-augmentation](./data_preprocessing/data-augmentation.ipynb) notebook. 
> The DataSet is avilable upon request just ping me on mail or twitter go to [contacts section](#contacts-or-for-more-info).

## Training the Model
> The Project is **still under development**, the model performs good in the testSet it gets more than 90% accuracy but all the problems comes from the data distribution, so the model will be retrainded on the second release.
- I used mobilenet (for transefer learning) from keras application layer.
- I freezed all the model's layers except the last 10 layers for tuning.
- In most cases with Transefer learning the model become prone to overfitting and that what happened with me:
  - So to overcome this problem **I just added an L2 regularization for the last ten layers.** you can refer to the model training notebook in the reqularization section. 

## Installation Instructions
1. Install python3 
2. Install pip3 `$ sudo apt install python3-pip`
3. Install virtualenv `$ python3 -m pip install --user virtualenv`
4. Append virtualenv path to your `$PATH varibale`
    - find out where virtualenv installed `$ which virtualenv`
    - append the output of the above command to `$ export PATH=/the/output/path:$PATH`
    - For more info regarding virtualenv tool you can visit this [github gist](https://gist.github.com/amshrbo/2ca0afb88c428b79ddaf38374226b9e0)
5. Clone the repo `$ git clone https://github.com/amshrbo/nsfw-detection.git`
6. Create the virtualenv `$ virtualenv --python=$(which python3) venv`
    - Make sure you are in the repo folder.
7. Activate virtualenv `$ source venv/bin/activate`
8. Install requirments `$ pip3 install -r requirments.txt`
9. Make sure that the version of pillow lib is Pillow==8.2.0
    - `$ pip freeze | grep Pillow`
    - As there is some lib conflicts with other pillow versions
    - To make sure that everything is okay `$ pip install Pillow==8.2.0`
10. run the app `$ python3 app.py`

## To Do
1. Collecting more violence data from this dataset in kaggle [real life violence](https://www.kaggle.com/mohamedmustafa/real-life-violence-situations-dataset)
    - This is a video dataset, so you can just extract frames from the videos.
1. In the next release you can drop the drugs class as it was very hard to collect images for it and didn't get a good accuracy after all
1. Retraining the model on this new dataset.
1. **Using more robust model** like resnet or vggnet instead of mobilenet. 

## Lessons from this project
- How to use keras ImageDateGenerator for doing data augmentation you can refer to [data augmentation notebook](./data_preprocessing/data-augmentation.ipynb)
- `np.shuffle()` shuffles every element in the array and doesn't respect the dimensions, so don't use it to shuffle multi-dims data
  - Just use the shuffle param in the `train_test_split()` or use the shuffle param in `keras.model.fit()`
- How to freeze a set of layers and keep the rest for training.
- How to add regularization (especially `l2`) to a trained model refer to [regularization section in this notebook](./training_and_loading/nsfw_detection_training.ipynb)
- If GitHub is unable to open any of the notebooks included in this project just use [nbviewer](https://nbviewer.jupyter.org/)
- To download batch images from any website use [Image Downloader chrome extension](https://chrome.google.com/webstore/detail/image-downloader/cnpniohnfphhjihaiiggeabnkjhpaldj)

## Contacts or for more info
> You can reach out to me in twitter [`@amshrbo`](https://twitter.com/amshrbo) or via mail `amshrbo@gmail.com`

## License
[GPL-3.0 License](./LICENSE)
