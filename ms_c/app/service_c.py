from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def response():
    return jsonify(
        ms_c=["Intentional", "Error", "500"],
    ),500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5002')