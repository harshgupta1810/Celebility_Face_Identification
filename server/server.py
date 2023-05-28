from flask import Flask, request, jsonify
import sklearn
import util

app = Flask(__name__)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    try:
        util.load_saved_artifacts()
        app.run(port=5000)
    except ModuleNotFoundError:
        print("Required modules not found. Please make sure scikit-learn is installed.")
