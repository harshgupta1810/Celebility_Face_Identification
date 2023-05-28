from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'hi'
if __name__ == "__main__":
    app.run(port=5000,debug=True)