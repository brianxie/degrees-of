from pymongo import MongoClient
import json

# done
def kill_all():
    client = MongoClient()
    db_list = client.database_names()
    for db in db_list:
        client.drop_database(db)
    return True

# done
def register_name(uuid, name):
    name_entry = {}
    name_entry["_id"] = uuid
    name_entry["name"] = name

    client = MongoClient()
    names = client.names # database names

    result = names.all.update_one({"_id": uuid}, {"$set": name_entry}, upsert=True)
    return result

# done
## PUBLIC API
def get_name(uuid):
    client = MongoClient()
    names = client.names # database names
    result = names.all.find_one({"_id": uuid}) # searches just by uuid; at most one match
    return result

# done
def get_all_names():
    client = MongoClient()
    names = client.names # database names
    cursor = names.all.find()
    documents = []
    for document in cursor:
        documents.append(document)
    return documents

# done
def register_user_data(user): # a "user" is the output of create_user_data
    # should update users table in mongodb, or add a new one
    client = MongoClient()
    users = client.users # database users
    # don't use insert to avoid duplicate key error
    # $setOnInsert?
    key = {}
    key["_id"] = user["_id"]
    result = users.all.update_one(key, {"$set": user}, upsert=True)
    return result

# done
## PUBLIC API
def create_user_data(name, uuid, is_artist):
    # initializes the (json? bson? python thing?) that characterizes a user
    # see user-data-schema
    user_data = {}
    user_data["_id"] = uuid
    user_data["is_artist"] = is_artist
    user_data["artist_scores"] = []
    if is_artist:
        artist_entry = {}
        artist_entry["_id"] = uuid
        artist_entry["distance"] = 0
        user_data["artist_scores"].append(artist_entry)
    user_data["neighbors"] = []

    register_name(uuid, name)
    register_user_data(user_data)

    # user_json = json.dumps(user_data)
    # return user_json
    return user_data

# done
## PUBLIC API
def get_user_entry(uuid): # queries users db
    client = MongoClient()
    users = client.users # database users
    result = users.all.find_one({"_id": uuid}) # searches just by uuid; at most one match
    return result

# done
def get_all_users(): # queries users
    client = MongoClient()
    users = client.users # database users
    cursor = users.all.find()
    documents = []
    for document in cursor:
        documents.append(document)
    return documents


# done
def get_neighbors(user):
    # retrieve list of neighbors (1-neighbors, a la adjacency list)
    neighbors = user["neighbors"]
    return neighbors

#done
def get_neighbor_uuid_set(user):
    neighbors = get_neighbors(user)
    neighbor_uuid_set = set()
    for neighbor in neighbors:
        neighbor_uuid_set.add(neighbor["_id"])
    return neighbor_uuid_set

# done
## PUBLIC API
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

# done
def add_neighbor(src_user, dst_user):
    # adds dst as a neighbor of src; does not handle artist logic
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


# done
def update_required(target, caller):
    # checks if we should add this node to the stack
    target_artist_scores_list = target["artist_scores"]
    caller_artist_scores_list = caller["artist_scores"]

    target_map = {}
    for artist_score in target_artist_scores_list:
        target_map[artist_score["_id"]] = artist_score["distance"]
    caller_map = {}
    for artist_score in caller_artist_scores_list:
        caller_map[artist_score["_id"]] = artist_score["distance"]

    for caller_key in caller_map.keys():
        if not caller_key in target_map:
            return True
        elif target_map[caller_key] > caller_map[caller_key] + 1:
            return True
    return False


    # neighbors = get_neighbors(target)
    # neighbor_list = []
    # for neighbor in neighbors:
    #     neighbor_list.append(get_user_entry(neighbor["_id"]))
    # return True

# done
def update_node(target, caller): # or user? should this query mongo?
    # this needs to handle artist logic
    target_artist_scores_list = target["artist_scores"]
    caller_artist_scores_list = caller["artist_scores"]

    target_map = {}
    for artist_score in target_artist_scores_list:
        target_map[artist_score["_id"]] = artist_score["distance"]
    caller_map = {}
    for artist_score in caller_artist_scores_list:
        caller_map[artist_score["_id"]] = artist_score["distance"]

    for caller_key in caller_map.keys():
        if not caller_key in target_map:
            artist_score = {}
            artist_score["_id"] = caller_key
            artist_score["distance"] = caller_map[caller_key] + 1
            target["artist_scores"].append(artist_score)
        elif target_map[caller_key] > caller_map[caller_key] + 1:
            artist_score = {}
            artist_score["_id"] = caller_key
            artist_score["distance"] = caller_map[caller_key] + 1
            for i in range(len(target["artist_scores"])):
                entry = target["artist_scores"][i]
                if entry["_id"] == caller_key:
                    target["artist_scores"][i] = artist_score
                    break



    # call get_neighbors and get list of neighbors
    # for each neighbor, call get_artist_scores; see if this node should be updated
    # for each neighbor, check if neighbor node also needs to be updated
    # if so, recursively call update_node on that node
    return None # TODO

# done
## PUBLIC API
def make_connection(uuid_1, uuid_2):
    if uuid_1 == uuid_2: # can't add yourself!
        return False

    IS_ARTIST_CONST = False # always assume that any new node is not an artist

    # query mongo for users
    user_1 = get_user_entry(uuid_1)
    user_2 = get_user_entry(uuid_2)

    # create users with NO_NAME if they don't yet exist
    # this should NOT HAPPEN; create_user_data should always be called first
    # this stores uuid:name mapping in some other database
    if user_1 == None:
        name_1 = get_name(uuid_1)
        if name_1 == None:
            name_1 = "NO_NAME"
        else:
            name_1 = name_1["name"]
        print(uuid_1)
        user_1 = create_user_data(name_1, uuid_1, IS_ARTIST_CONST)
    if user_2 == None:
        name_2 = get_name(uuid_2)
        if name_2 == None:
            name_2 = "NO_NAME"
        else:
            name_2 = name_2["name"]
        user_2 = create_user_data(name_2, uuid_2, IS_ARTIST_CONST)

    # add_neighbor on each node
    new_entry_created_1 = add_neighbor(user_1, user_2)[1]
    new_entry_created_2 = add_neighbor(user_2, user_1)[1]

    if not new_entry_created_1 and not new_entry_created_2: # already connected
        return False

    register_user_data(user_1)
    register_user_data(user_2)


    # # if users already connected, terminate early
    # # this block is kinda handled by add_neighbor already
    # user_1_neighbors = get_neighbors(user1)
    # user_2_neighbors = get_neighbors(user2)

    # user_1_neighbors_uuid_list = []
    # user_2_neighbors_uuid_list = []
    # for item in user_1_neighbors:
    #     user_1_neighbors_uuid_list.append(item["_id"])
    # for item in user_2_neighbors:
    #     user_2_neighbors_uuid_list.append(item["_id"])

    # if uuid_1 in user_2_neighbors_uuid_list or uuid_2 in user_1_neighbors_uuid_list:
    #     return False

    # call update_node on both nodes and any other required nodes

    update_pq = [] # tuples of uuid, caller uuid
    if update_required(user_1, user_2):
        update_pq.insert(0, (uuid_1, uuid_2))
    if update_required(user_2, user_1):
        update_pq.insert(0, (uuid_2, uuid_1))

    while len(update_pq) > 0:
        entry = update_pq.pop()
        target_uuid = entry[0]
        caller_uuid = entry[1]
        target = get_user_entry(target_uuid)
        caller = get_user_entry(caller_uuid)

        update_node(target, caller)
        target_neighbor_uuid_set = get_neighbor_uuid_set(target)
        target_neighbor_uuid_set.remove(caller_uuid) # can't modify own caller
        for neighbor_uuid in target_neighbor_uuid_set:
            neighbor = get_user_entry(neighbor_uuid)
            if update_required(neighbor, target):
                update_pq.insert(0, (neighbor_uuid, target_uuid))

        register_user_data(target)


    return True
