from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from CNNClassifier.utils.common import decodeImage
from CNNClassifier.pipeline.prediction import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientAPP:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train",methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "Training done sucessfully"

@app.route("/predict",methods=['POST'])
@cross_origin()
def predictionRoute():
    image = request.json['image']
    decodeImage(image, clAPP.filename)
    result = clAPP.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    clAPP = ClientAPP()
    app.run(host='0.0.0.0', port=8080) #local host
    # app.run(host='0.0.0.0', port=8080) #for aws
    # app.run(host='0.0.0.0', port=80) #for azure








