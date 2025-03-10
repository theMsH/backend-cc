from flask import Flask, request
import pickle
from sklearn.pipeline import Pipeline

with open("./assets/model.pkl", "rb") as f:
    model: Pipeline = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Sentiment backend v1</h1>"

@app.route("/sentiment", methods=["POST"])
def get_sentiment():
    input_data = request.json
    sentiment = model.predict([input_data])[0]
    return {'input_data': input_data, 'sentiment': sentiment}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=False)