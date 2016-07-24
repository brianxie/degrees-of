from pymongo import MongoClient

def add_user(uuid, is_artist): # string, bool; queries users
    # should update users table in mongodb
    client = MongoClient()
    users = client.users # database users
    # don't use insert to avoid duplicate key error
    # result = users.all.insert_one({"_id": uuid, "is_artist": is_artist}) # collection all (only has one)
    result = users.all.update_one({"_id": uuid, "is_artist": is_artist}, {"$setOnInsert": {"_id": uuid, "is_artist": is_artist}}, upsert=True)
    return result

def get_user(uuid): # queries users
    client = MongoClient()
    users = client.users # database users
    result = users.all.find_one({"_id": uuid})
    return result

def get_all_users(): # queries users
    client = MongoClient()
    users = client.users # database users
    cursor = users.all.find()
    documents = []
    for document in cursor:
        documents.append(document)
    return documents

def get_neighbors(uuid):
    # query mongodb, retrieve list of neighbors
    client = MongoClient()
    return None

def get_distances(uuid):
    # get distances to all artists for given uuid
    # just a mongodb query
    return None

def add_neighbor(src, dst):
    # adds dst as a neighbor of src
    return None

def update_node(uuid):
    # call get_neighbors and get list of neighbors
    # for each neighbor, call get_distances; see if this node should be updated
    # for each neighbor, check if neighbor node also needs to be updated
    # if so, recursively call uuid on that node
    return None # TODO

def make_connection(uuid1, uuid2):
    # if a user not in table, add_user
    # if connection already exists, terminate - nothing to do
    # add_neighbor on each node
    # call update_node on both nodes
    return None # TODO
