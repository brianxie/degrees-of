from pymongo import MongoClient
import json

def get_user(uuid): # queries users db
    client = MongoClient()
    users = client.users # database users
    result = users.all.find_one({"_id": uuid}) # searches just by uuid; at most one match
    return result

def get_all_users(): # queries users
    client = MongoClient()
    users = client.users # database users
    cursor = users.all.find()
    documents = []
    for document in cursor:
        documents.append(document)
    return documents

def get_neighbors(user):
    # retrieve list of neighbors (1-neighbors, a la adjacency list)
    neighbors = user["neighbors"]
    return neighbors

def get_distances(user):
    # get distances to all artists for given uuid
    return None

def create_user_data(uuid, is_artist):
    # initializes the (json? bson? python thing?) that characterizes a user
    # see user-data-schema
    user_data = {}
    user_data["_id"] = uuid
    user_data["is_artist"] = is_artist
    user_data["artist_scores"] = []
    user_data["neighbors"] = []
    # user_json = json.dumps(user_data)
    # return user_json
    return user_data

def add_user(uuid, is_artist): # string, bool; queries users
    # should update users table in mongodb
    client = MongoClient()
    users = client.users # database users
    # don't use insert to avoid duplicate key error
    user_data = create_user_data(uuid, is_artist)
    result = users.all.update_one(user_data, {"$setOnInsert": user_data}, upsert=True)
    return result


def add_neighbor(src, dst):
    # adds dst as a neighbor of src
    return None

def update_node(uuid): # or user? should this query mongo?
    # call get_neighbors and get list of neighbors
    # for each neighbor, call get_distances; see if this node should be updated
    # for each neighbor, check if neighbor node also needs to be updated
    # if so, recursively call update_node on that node
    return None # TODO

def make_connection(uuid1, uuid2):
    # if a user not in table, add_user
    # if connection already exists, terminate - nothing to do
    # add_neighbor on each node
    # call update_node on both nodes
    return None # TODO
