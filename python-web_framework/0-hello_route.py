"""dmdsfjfjdsf;ksjdf;ksdjf;sdkfjksdfjkdfjdlfjdkfjdfkd;sjf;fjks;dlfksd;lfksdfk;sdlfk;sdlk"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """jijfwekfjm;dfmvdv;dmerfjgmpd;vmpvl;sovekgporgmvvmpos"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
