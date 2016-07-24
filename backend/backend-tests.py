from pymongo import MongoClient

import sys
sys.path.append("./flask/")
from flasklib import *

# constants
UUID_1 = "0000000000"
UUID_2 = "9999999999"

client = MongoClient()
users = client.users # database users
# userinfo = client.userinfo # database userinfo

result = create_user_data(UUID_1, False)
# print(result)

result = add_user(UUID_1, False)
# print(result)
result = add_user(UUID_2, False)
# print(result)


result = get_user(UUID_1)
# print(result)
result = get_all_users()
# print(result)

USER_1 = get_user(UUID_1)
result = get_neighbors(USER_1)
print(result)






# get_distances
# add_neighbor
# update_node
# make_connection
