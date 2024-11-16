from flask import Flask, render_template, request
from model import predict_image
import utils

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print(prediction)
            result = utils.disease_dic.get(prediction, "Unknown")
            return render_template('display.html', status=200, result=result)
        except Exception as e:
            print(e)  # Print any exception for debugging
            return render_template('index.html', status=500, result="Internal Server Error")
    return render_template('index.html', status=405, result="Method Not Allowed")

if __name__ == "__main__":
    app.run(debug=True)
