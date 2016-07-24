from flask import Flask, request
from pymongo import MongoClient

from flasklib import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "GET":
        print("get")
    elif request.method == "POST":
        print("post")
    else:
        print("no")
    # print(json.loads(request.data))
    print(request.data)

    return "brian\nkevin\nrahul"

# TODO http requests

@app.route("/getname/<uuid>")
def getName(uuid):
    return json.dumps(get_name(uuid))

@app.route("/createuserdata/<name>/<uuid>/<isartist>")
def createUserData(name, uuid, isartist):
    return json.dumps(create_user_data(name, uuid, isartist))

@app.route("/getuserentry/<uuid>")
def getUserEntry(uuid):
    return json.dumps(get_user_entry(uuid))

@app.route("/getartistscores/<uuid>")
def getArtistScores(uuid):
    user = get_user_entry(uuid)
    return json.dumps(get_artist_scores(user))

@app.route("/makeconnection/<uuid1>/<uuid2>")
def makeConnection(uuid1, uuid2):
    return make_connection(uuid1, uuid2)


if __name__ == "__main__":
    app.run(host="0.0.0.0")



# dead
# def recompute_graph(): # not required if we graph is built incrementally (?)
#     # creates graph from edge tables? floyd-warshall?
#     return None # TODO
