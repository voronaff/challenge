from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    raise Exception('Something wrong in microservice C')

if __name__ == '__main__':
    app.run(debug=True, port=5002)