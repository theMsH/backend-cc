from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello world!</h1>"

@app.route("/sentiment", methods=["POST"])
def get_sentiment():
    input_data = request.json
    sentiment = 'neutral'
    return {'input_data': input_data, 'sentiment': sentiment}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=False)