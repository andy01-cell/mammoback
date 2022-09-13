import base64
from flask import Flask, request, json,jsonify
import os
import numpy as np
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pydicom
from PIL import Image
from werkzeug.utils import secure_filename
from flask_cors import CORS
import cv2

my_awesome_app = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    resp = jsonify({'message': 'Ping andy'})
    resp.status_code = 201
    return resp


@my_awesome_app.route('/getfile')
def getfile():
    with open("kanker.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    print("imags", image_file)
    return image_file


if __name__ == '__main__':
    my_awesome_app.run()
