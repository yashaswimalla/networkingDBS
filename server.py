from flask import Flask

PORT = 80
MESSAGE = "Hello, world! \n Thank you for coming till the end of our presentation. \n"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
