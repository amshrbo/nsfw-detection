from flask import Flask, request, jsonify
import werkzeug
from PIL import Image
import os, shutil
from helpers.nsfwDetection import nsfw_detection
from helpers.nudityDetection import nude_detection
from helpers.nsfwCheck import nsfw_check

savingFolder = './uploadedImgs'
app = Flask(__name__)

def get_preds(img_path):
    value = nude_detection(img_path)
    nsfw_preds = nsfw_detection(img_path)

    unsafe_score = value[img_path]['unsafe']
    unsafe_score = int(unsafe_score * 100)    

    isContainNudity = False
    if unsafe_score > 85:
        isContainNudity = True

    preds = {
        'nude_score': unsafe_score,
        # 'drugs_score': int(nsfw_preds[0][0] * 100),
        'violence_score': int(nsfw_preds[0][1] * 100),
        'natural_score': int(nsfw_preds[0][2] * 100)
    }

    return preds


@app.route('/', methods=['POST', 'GET'])
def hello():
    return 'Hello world'

@app.route('/preds', methods=['POST', 'GET'])
def uploaded_imgs():

    img_files_ids = request.files.getlist('images')
    print(f"____The number of Imgs is {len(img_files_ids)}____")

    all_results = []    
    for img_file in request.files.getlist('images'):
        img_name = werkzeug.utils.secure_filename(img_file.filename)
        print(f'Recived an img with file name: {img_name}')
        img_path = os.path.join(savingFolder, img_name)
        img_file.save(img_path)

        predictions = get_preds(img_path)
        print(predictions)
        result = {'img_path': img_path, 'preds':predictions}

        all_results.append(result)

    print(all_results)

    print("___Deleting files____")
    delete_imgs()

    boleans = nsfw_check(all_results)
    print(boleans)

    return jsonify(
        data = all_results,
        isContainNude = boleans['nude'], 
        isContainViolence = boleans['violence']
        # isContainDrugs = boleans['drugs']
        )


def delete_imgs():
    for imgname in os.listdir(savingFolder):
        img_path = os.path.join(savingFolder, imgname)
        os.remove(img_path)


if __name__ == '__main__':
    app.run(debug=True)

"""
curl -i -H "Content-Type: application/json" -X POST -d '{"img_path":"/home/shrbo/Downloads/dtest.jpeg"}' http:/localhost:5000/img_path
"""