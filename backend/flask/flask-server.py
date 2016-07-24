from flask import Flask, request
from pymongo import MongoClient

from flasklib import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    # print(json.loads(request.data))
    # print(request.data)
    return "brian\nkevin\nrahul"

# @app.route("/getname/<uuid>")
# def getName(uuid):
@app.route("/getname/", methods=["GET"])
def getName():
    query = request.args
    uuid = query["uuid"]
    return json.dumps(get_name(uuid))

# @app.route("/getuserentry/<uuid>")
# def getUserEntry(uuid):
@app.route("/getuserentry/", methods=["GET"])
def getUserEntry():
    query = request.args
    uuid = query["uuid"]
    return json.dumps(get_user_entry(uuid))

# @app.route("/getartistscores/<uuid>")
# def getArtistScores(uuid):
@app.route("/getartistscores/", methods=["GET"])
def getArtistScores():
    query = request.args
    uuid = query["uuid"]
    user = get_user_entry(uuid)
    return json.dumps(get_artist_scores(user))

# @app.route("/createuserdata/<name>/<uuid>/<isartist>")
# def createUserData(name, uuid, isartist):
@app.route("/createuserdata/", methods=["POST"])
def createUserData():
    query = request.form.to_dict()
    name = query["name"]
    uuid = query["uuid"]
    is_artist = query["is_artist"]
    return json.dumps(create_user_data(name, uuid, is_artist))

# @app.route("/makeconnection/<uuid1>/<uuid2>")
# def makeConnection(uuid1, uuid2):
@app.route("/makeconnection/", methods=["GET"])
def makeConnection():
    query = request.form.to_dict()
    print(query)
    uuid_1 = query["uuid_1"]
    uuid_2 = query["uuid_2"]
    return json.dumps(make_connection(uuid_1, uuid_2))


if __name__ == "__main__":
    app.run(host="0.0.0.0")


# dead
# def recompute_graph(): # not required if we graph is built incrementally (?)
#     # creates graph from edge tables? floyd-warshall?
#     return None # TODO
