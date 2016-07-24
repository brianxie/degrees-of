from flask import Flask
from pymongo import MongoClient

from flasklib import *

app = Flask(__name__)


@app.route("/")
def root():
    return "brian\nkevin\nrahul"

if __name__ == "__main__":
    app.run()



# dead
def recompute_graph(): # not required if we graph is built incrementally (?)
    # creates graph from edge tables? floyd-warshall?
    return None # TODO
