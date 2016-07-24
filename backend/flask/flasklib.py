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

def add_user(user): # a "user" is the output of create_user_data
    # should update users table in mongodb, or add a new one
    client = MongoClient()
    users = client.users # database users
    # don't use insert to avoid duplicate key error
    # $setOnInsert?
    result = users.all.update_one(user, {"$set": user}, upsert=True)
    return result

def get_neighbors(user):
    # retrieve list of neighbors (1-neighbors, a la adjacency list)
    neighbors = user["neighbors"]
    return neighbors

def get_artist_scores(user):
    # get distances to all artists for given uuid
    # note that the schema stores the exact path, but this method is not interested
    artist_scores = user["artist_scores"]

    # distances = []
    # for artist_entry in artist_scores:
    #     distance_entry = {}
    #     distance_entry["_id"] = artist_entry["_id"]
    #     distance_entry["distance"] = artist_entry["distance"]
    #     # ignore the shortest path; we don't want that

    return artist_scores

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


def add_neighbor(src_user, dst_user):
    # adds dst as a neighbor of src
    dst_id = dst_user["_id"]
    src_user_neighbors = src_user["neighbors"] # list of "_id": id

    new_entry_required = True

    for neighbor in src_user_neighbors: # each neighbor is a dictionary
        neighbor_id = neighbor["_id"]
        if neighbor_id == dst_id:
            new_entry_required = False
            break

    if new_entry_required:
        new_neighbor = {}
        new_neighbor["_id"] = dst_id
        src_user_neighbors.append(new_neighbor)

    return (src_user, new_entry_required)

def update_required(user):
    # checks if we should add this node to the stack
    return None

def update_node(user, caller): # or user? should this query mongo?
    # call get_neighbors and get list of neighbors
    # for each neighbor, call get_artist_scores; see if this node should be updated
    # for each neighbor, check if neighbor node also needs to be updated
    # if so, recursively call update_node on that node
    return None # TODO

def make_connection(uuid1, uuid2):
    IS_ARTIST_CONST = False

    user_1 = get_user(uuid1)
    user_2 = get_user(uuid2)

    # add users to database if they don't yet exist
    requery1 = False
    requery2 = False
    if user_1 == None:
        add_user(create_user_data(uuid1, IS_ARTIST_CONST))
    if user_2 == None:
        add_user(create_user_data(uuid2, IS_ARTIST_CONST))

    if requery1:
        user_1 = get_user(uuid1)
    if requery2:
        user_2 = get_user(uuid2)

    # if users already connected, terminate early
    user_1_neighbors = get_neighbors(user1)
    user_2_neighbors = get_neighbors(user2)

    user_1_neighbors_uuid_list = []
    user_2_neighbors_uuid_list = []
    for item in user_1_neighbors:
        user_1_neighbors_uuid_list.append(item["_id"])
    for item in user_2_neighbors:
        user_2_neighbors_uuid_list.append(item["_id"])

    if uuid1 in user_2_neighbors_uuid_list or uuid2 in user_1_neighbors_uuid_list:
        return False

    # add_neighbor on each node
    # call update_node on both nodes
    return None # TODO
