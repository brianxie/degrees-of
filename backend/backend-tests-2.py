from pymongo import MongoClient

import sys
sys.path.append("./flask/")
from flasklib import *

#constant UUIDs
UUID_1 = "010101010"	# J. Cole
UUID_2 = "101010101"	# Lana Del Rey
UUID_3 = "123123123"	# Rahul
UUID_4 = "231231231"	# Brian
UUID_5 = "312312312"	# Kevin
UUID_6 = "917115116"	# Claremont ("NO_NAME")

client = MongoClient()
users = client.users
names = client.names

USER_1 = create_user_data("jcole", UUID_1, True)
USER_3 = create_user_data("rahul", UUID_3, False)
USER_4 = create_user_data("brian", UUID_4, False)
USER_5 = create_user_data("kevin", UUID_5, False)
USER_6 = create_user_data("claremont", UUID_6, False)


result = make_connection(UUID_1, UUID_6)				# connection between jcole and NO_NAME
print ("This should print True: " + str(result))
result = make_connection(UUID_1, UUID_6)
print ("This should print False: " + str(result))

print ("--- This is NO_NAME's scores")
print (get_artist_scores(USER_6))							# NO_NAME's score for jcole should be 1, and lana should not exist
print ("--- This is jcole's scores")
print (get_artist_scores(USER_1))							# jcole's score for himself should be 0, and lana should not exist

result = make_connection(UUID_3, UUID_1)				# connection between rahul and jcole
print ("This should print True: " + str(result))
result = make_connection(UUID_1, UUID_3)
print ("This should print False: " + str(result))

print ("--- This is rahul's scores")
print (get_artist_scores(USER_3))							# rahul's score for jcole should be 1, and lana should not exist
print ("--- This is jcole's scores")
print (get_artist_scores(USER_1))							# jcole's score for himself should be 0, and lana should not exist

result = make_connection(UUID_4, UUID_1)				# connection between brian and jcole
print("This shoudl print True: " + str(result))
result = make_connection(UUID_1, UUID_4)
print ("This should print False: " + str(result))

print ("--- This is brian's scores")
print (get_artist_scores(USER_4)	)						# brian's score for jcole should be 1, and lana should not exist
print ("--- This is jcole's scores")
print (get_artist_scores(USER_1))							# jcole's score for himself should be 0, and lana should not exist

USER_2 = create_user_data("lana", UUID_2, True)			# Lana Del Rey is created

result = make_connection(UUID_2, UUID_5)				# connection between lana and kevin
print ("This should print True: " + str(result))
result = make_connection(UUID_5, UUID_2)
print ("This should print False: " + str(result))

print ("--- This is rahul's scores ---")
print (get_artist_scores(USER_3))						# rahul's score for jcole should be 1, and lana should not exist
print ("--- This is NO_NAME's scores")
print (get_artist_scores(USER_6))						# NO_NAME's score for jcole should be 1, and lana should not exist
print ("--- This is kevin's scores")
print (get_artist_scores(UUID_5))						# kevin's score for jcole should not exist, and lana should be 1
print ("--- This is brian's scores")
print (get_artist_scores(USER_4))						# brian's score for jcole should be 1, and lana should not exist
print ("--- This is jcole's score")
print (get_artist_scores(USER_1))						# jcole's score for himself should be 0, and lana should not exist
print ("--- This is lana's score")
print (get_artist_scores(USER_2))						# lana's score for jcole should not exist, and for herself should be 0

result = make_connection(UUID_3, UUID_5)			# connection between rahul and kevin
print ("This should print True: " + str(result))

print ("--- This is rahul's scores ---")
print (get_artist_scores(USER_3))						# rahul's score for jcole should be 1, and lana should be 2
print ("--- This is NO_NAME's scores")
print (get_artist_scores(USER_6))						# NO_NAME's score for jcole should be 1, and lana should be 3
print ("--- This is kevin's scores")
print (get_artist_scores(UUID_5))						# kevin's score for jcole should be 2, and lana should be 1
print ("--- This is brian's scores")
print (get_artist_scores(USER_4))						# brian's score for jcole should be 1, and lana should not exist
print ("--- This is jcole's score")
print (get_artist_scores(USER_1))						# jcole's score for himself should be 0, and lana should be 3
print ("--- This is lana's score")
print (get_artist_scores(USER_2))						# lana's score for jcole should be 3, and for herself should be 0

result = make_connection(UUID_3, UUID_5)
print ("This should print False: " + str(result))

result = make_connection(UUID_3, UUID_2)				# connection between rahul and lana
print ("This should print True: " + str(result))
result = make_connection(UUID_2, UUID_3)
print ("This should print False: " + str(result))

print ("--- This is rahul's scores ---")
print (get_artist_scores(USER_3))						# rahul's score for jcole should be 1, and lana should be 1
print ("--- This is NO_NAME's scores")
print (get_artist_scores(USER_6))						# NO_NAME's score for jcole should be 1, and lana should be 2
print ("--- This is kevin's scores")
print (get_artist_scores(UUID_5))						# kevin's score for jcole should be 2, and lana should be 1
print ("--- This is brian's scores")
print (get_artist_scores(USER_4))						# brian's score for jcole should be 1, and lana should not exist
print ("--- This is jcole's score")
print (get_artist_scores(USER_1))						# jcole's score for himself should be 0, and lana should be 2
print ("--- This is lana's score")
print (get_artist_scores(USER_2))						# lana's score for jcole should be 2, and for herself should be 0

result = make_connection(UUID_3, UUID_4)				# connection between rahul and brian
print ("This should print True: " + str(result))
result = make_connection(UUID_3, UUID_4)
print ("This should print False: " + str(result))

print ("--- This is rahul's scores ---")
print (get_artist_scores(USER_3))						# rahul's score for jcole should be 1, and lana should be 1
print ("--- This is NO_NAME's scores")
print (get_artist_scores(USER_6))						# NO_NAME's score for jcole should be 1, and lana should be 2
print ("--- This is kevin's scores")
print (get_artist_scores(UUID_5))						# kevin's score for jcole should be 2, and lana should be 1
print ("--- This is brian's scores")
print (get_artist_scores(USER_4))						# brian's score for jcole should be 1, and lana should be 2
print ("--- This is jcole's score")
print (get_artist_scores(USER_1))						# jcole's score for himself should be 0, and lana should be 2
print ("--- This is lana's score")
print (get_artist_scores(USER_2))						# lana's score for jcole should be 2, and for herself should be 0