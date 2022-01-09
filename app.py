from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import  get_response
app = Flask(__name__)
CORS(app)


@app.route("/predict", methods = ['POST', 'GET'])
def predict():  
    text = request.json.get('message')
    response = get_response(text)
    message = {"answer": response}
    if request.method == 'POST':
        return  jsonify(message)
    return 

if __name__ == '__main__':
    app.run(debug=True)