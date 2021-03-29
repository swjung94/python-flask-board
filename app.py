from flask import Flask
import config

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask'

if __name__ == "__main__":
    app.run(host="localhost", port=config.PORT, debug=config.DEBUG_MODE)
