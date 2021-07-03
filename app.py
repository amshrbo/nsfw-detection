from flask import Flask, request, jsonify
from PIL import Image
from helpers.nsfwDetection import nsfw_detection
from helpers.nudityDetection import nude_detection

app = Flask(__name__)

def get_preds(img_path):
    value = nude_detection(img_path)
    unsafe_score = value[img_path]['unsafe']
    
    nsfw_preds = nsfw_detection(img_path)
    preds = {
        'nude_score': int(unsafe_score * 100),
        'drugs_score': int(nsfw_preds[0][0] * 100),
        'violence_score': int(nsfw_preds[0][1] * 100),
        'natural_score': int(nsfw_preds[0][2] * 100)
    }
    # print(preds)

    return preds


@app.route('/img_path', methods=['POST'])
def uploaded_imgs():
    img_path = request.json['img_path']
    print(img_path)
    predictions = get_preds(img_path)

    print(predictions)
    print(type(predictions))
    result = [
        {'img_path': img_path, 'preds':predictions},
        {'img_path': img_path, 'preds':predictions} 
    ]

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

"""
curl -i -H "Content-Type: application/json" -X POST -d '{"img_path":"/home/shrbo/Downloads/dtest.jpeg"}' http:/localhost:5000/img_path
"""