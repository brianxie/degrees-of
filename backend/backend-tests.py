from pymongo import MongoClient

import sys
sys.path.append("./flask/")
from flasklib import *

UUID_1 = "0000000000"
UUID_2 = "9999999999"

client = MongoClient()

users = client.users # database users
userinfo = client.userinfo # database userinfo


# insert the data
result = add_user(UUID_1, False)
print(result)
result = users.all.insert_one({UUID_2: False}) # collection all
print(result)


