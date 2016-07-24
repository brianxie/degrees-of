from pymongo import MongoClient

import sys
sys.path.append("./flask/")
from flasklib import *

client = MongoClient()
users = client.users # database users
names = client.names # database names
