from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def root():
    return "brian\nkevin\nrahul"

if __name__ == "__main__":
    app.run()
