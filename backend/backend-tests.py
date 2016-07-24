from pymongo import MongoClient

import sys
sys.path.append("./flask/")
from flasklib import *

# constants
UUID_1 = "0000000000"
UUID_2 = "9999999999"

client = MongoClient()
users = client.users # database users
names = client.names # database names
# userinfo = client.userinfo # database userinfo
# TODO need to map uuids to names

USER_1 = create_user_data("brian", UUID_1, False)
print(USER_1)
USER_2 = create_user_data("kanye", UUID_2, True)
print(USER_2)
result = add_user(USER_2)
# print(result)
# result = get_user(UUID_1)
# print(result)
# result = get_user(UUID_2)
# print(result)


# result = get_artist_scores(USER_1)
# print(result)
# result = get_artist_scores(USER_2)
# print(result)

result = make_connection(UUID_1, UUID_2)
# print(result)
USER_1 = get_user(UUID_1)
print(get_artist_scores(USER_1))
print(get_artist_scores(USER_2))

print(get_all_users())


print(get_name(UUID_1))
print(get_name(UUID_2))


# result = get_user(UUID_1)
# print(result)

# result = add_user(USER_1)
# print(result)
# result = add_user(USER_2)
# print(result)

# result = get_user(UUID_1)
# print(result)
# result = get_user(UUID_2)
# print(result)

# result = add_user(USER_1)
# print(result)
# result = get_user(UUID_1)
# print(result)



# result = get_all_users()
# print(result)

# USER_1 = get_user(UUID_1)
# result = get_neighbors(USER_1)
# print(result)
# result = get_artist_scores(USER_1)
# print(result)

# result = add_neighbor(USER_1, USER_2)
# print(result)
# result = get_neighbors(USER_1)
# print(result)
# result = add_neighbor(USER_1, USER_2)
# print(result)
# result = get_neighbors(USER_1)
# print(result)


# result = make_connection(UUID_1, UUID_2)
# print(result)
# result = make_connection(UUID_1, UUID_2)
# print(result)



# add_neighbor
# update_node
# make_connection
