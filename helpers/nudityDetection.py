import os
from nudenet import NudeClassifierLite

print('----------Initializing the NudeClassifier----------')
clf = NudeClassifierLite()


def nude_detection(img_path):
    nudity_score = clf.classify(img_path)

    return nudity_score