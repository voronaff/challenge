from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def response():
    return jsonify(
        ms_b=["I'm", "alive"],
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001')