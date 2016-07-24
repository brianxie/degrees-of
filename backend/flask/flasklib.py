from pymongo import MongoClient

def add_user(uuid, is_artist): # string, bool
    # should update users table in mongodb
    client = MongoClient()
    users = client.users # database users
    result = users.all.insert_one({uuid: is_artist}) # collection all (only has one)
    return result # TODO

def get_neighbors(uuid):
    # query mongodb, retrieve list of neighbors
    return None

def get_distances(uuid):
    # get distances to all artists for given uuid
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
    # call update_node on both nodes
    return None # TODO
