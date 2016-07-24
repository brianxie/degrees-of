from pymongo import MongoClient

import sys
sys.path.append("./flask/")
from flasklib import *

#constant UUIDs
UUID_1 = "jcole"	# J. Cole
UUID_2 = "lana"	# Lana Del Rey
UUID_3 = "rahul"	# Rahul
UUID_4 = "brian"	# Brian
UUID_5 = "kevin"	# Kevin
UUID_6 = "claremont"	# Claremont ("NO_NAME")

client = MongoClient()
users = client.users
names = client.names

USER_1 = create_user_data("jcole", UUID_1, True)
USER_3 = create_user_data("rahul", UUID_3, False)
USER_4 = create_user_data("brian", UUID_4, False)
USER_5 = create_user_data("kevin", UUID_5, False)
USER_6 = create_user_data("claremont", UUID_6, False)

print ("=== ROUND 1 ===")
result = make_connection(UUID_1, UUID_6)				# connection between jcole and NO_NAME
print ("This should print True: " + str(result))
result = make_connection(UUID_1, UUID_6)
print ("This should print False: " + str(result))
print ("")

USER_6 = get_user_entry(UUID_6)
print ("--- This is NO_NAME's scores ---")
print (get_artist_scores(USER_6))						#NO_NAME's score for jcole should be 1, and lana should not exist
USER_1 = get_user_entry(UUID_1)
print ("--- This is jcole's scores ---")
print (get_artist_scores(USER_1))							# jcole's score for himself should be 0, and lana should not exist
print ("")

print("=== ROUND 2 ===")
result = make_connection(UUID_3, UUID_1)				# connection between rahul and jcole
print ("This should print True: " + str(result))
result = make_connection(UUID_1, UUID_3)
print ("This should print False: " + str(result))


USER_3 = get_user_entry(UUID_3)
print ("--- This is rahul's scores ---")
print (get_artist_scores(USER_3))							# rahul's score for jcole should be 1, and lana should not exist
USER_1 = get_user_entry(UUID_1)
print ("--- This is jcole's scores ---")
print (get_artist_scores(USER_1))						# jcole's score for himself should be 0, and lana should not exist
print ("")


print("=== ROUND 3 ===")
result = make_connection(UUID_4, UUID_1)				# connection between brian and jcole
print("This should print True: " + str(result))
result = make_connection(UUID_1, UUID_4)
print ("This should print False: " + str(result))

USER_4 = get_user_entry(UUID_4)
print ("--- This is brian's scores ---")
print (get_artist_scores(USER_4))							# brian's score for jcole should be 1, and lana should not exist
USER_1 = get_user_entry(UUID_1)
print ("--- This is jcole's scores ---")
print (get_artist_scores(USER_1))							# jcole's score for himself should be 0, and lana should not exist
print ("")

print ("=== ROUND 4 ===")
USER_2 = create_user_data("lana", UUID_2, True)			# Lana Del Rey is created
print ("LANA IS CREATED")

result = make_connection(UUID_2, UUID_5)				# connection between lana and kevin
print ("This should print True: " + str(result))
result = make_connection(UUID_5, UUID_2)
print ("This should print False: " + str(result))

USER_3 = get_user_entry(UUID_3)
print ("--- This is rahul's scores ---")
print (get_artist_scores(USER_3))						# rahul's score for jcole should be 1, and lana should not exist
USER_6 = get_user_entry(UUID_6)
print ("--- This is NO_NAME's scores ---")
print (get_artist_scores(USER_6))						# NO_NAME's score for jcole should be 1, and lana should not exist
USER_5 = get_user_entry(UUID_5)
print ("--- This is kevin's scores ---")
print (get_artist_scores(USER_5))						# kevin's score for jcole should not exist, and lana should be 1
USER_4 = get_user_entry(UUID_4)
print ("--- This is brian's scores ---")
print (get_artist_scores(USER_4))						# brian's score for jcole should be 1, and lana should not exist
USER_1 = get_user_entry(UUID_1)
print ("--- This is jcole's scores ---")
print (get_artist_scores(USER_1))						# jcole's score for himself should be 0, and lana should not exist
USER_2 = get_user_entry(UUID_2)
print ("--- This is lana's scores ---")
print (get_artist_scores(USER_2))						# lana's score for jcole should not exist, and for herself should be 0
print ("")


print("=== ROUND 5 ===")
result = make_connection(UUID_3, UUID_5)			# connection between rahul and kevin
print ("This should print True: " + str(result))

USER_3 = get_user_entry(UUID_3)
print ("--- This is rahul's scores ---")
print (get_artist_scores(USER_3))						# rahul's score for jcole should be 1, and lana should be 2
USER_6 = get_user_entry(UUID_6)
print ("--- This is NO_NAME's scores ---")
print (get_artist_scores(USER_6))						# NO_NAME's score for jcole should be 1, and lana should be 4
USER_5 = get_user_entry(UUID_5)
print ("--- This is kevin's scores ---")
print (get_artist_scores(USER_5))						# kevin's score for jcole should be 2, and lana should be 1
USER_4 = get_user_entry(UUID_4)
print ("--- This is brian's scores ---")
print (get_artist_scores(USER_4))						# brian's score for jcole should be 1, and lana should be 4
USER_1 = get_user_entry(UUID_1)
print ("--- This is jcole's scores ---")
print (get_artist_scores(USER_1))						# jcole's score for himself should be 0, and lana should be 3
USER_2 = get_user_entry(UUID_2)
print ("--- This is lana's scores ---")
print (get_artist_scores(USER_2))						# lana's score for jcole should be 3, and for herself should be 0
print ("")

print("=== ROUND 6 ===")
result = make_connection(UUID_3, UUID_5)
print ("This should print False: " + str(result))

result = make_connection(UUID_3, UUID_2)				# connection between rahul and lana
print ("This should print True: " + str(result))
result = make_connection(UUID_2, UUID_3)
print ("This should print False: " + str(result))

USER_3 = get_user_entry(UUID_3)
print ("--- This is rahul's scores ---")
print (get_artist_scores(USER_3))						# rahul's score for jcole should be 1, and lana should be 1
USER_6 = get_user_entry(UUID_6)
print ("--- This is NO_NAME's scores ---")
print (get_artist_scores(USER_6))						# NO_NAME's score for jcole should be 1, and lana should be 3
USER_5 = get_user_entry(UUID_5)
print ("--- This is kevin's scores ---")
print (get_artist_scores(USER_5))						# kevin's score for jcole should be 2, and lana should be 1
USER_4 = get_user_entry(UUID_4)
print ("--- This is brian's scores ---")
print (get_artist_scores(USER_4))						# brian's score for jcole should be 1, and lana should be 3
USER_1 = get_user_entry(UUID_1)
print ("--- This is jcole's scores ---")
print (get_artist_scores(USER_1))						# jcole's score for himself should be 0, and lana should be 2
USER_2 = get_user_entry(UUID_2)
print ("--- This is lana's scores ---")
print (get_artist_scores(USER_2))						# lana's score for jcole should be 2, and for herself should be 0
print ("")


print("=== ROUND 7 ===")
result = make_connection(UUID_3, UUID_4)				# connection between rahul and brian
print ("This should print True: " + str(result))
result = make_connection(UUID_3, UUID_4)
print ("This should print False: " + str(result))

USER_3 = get_user_entry(UUID_3)
print ("--- This is rahul's scores ---")
print (get_artist_scores(USER_3))						# rahul's score for jcole should be 1, and lana should be 1
USER_6 = get_user_entry(UUID_6)
print ("--- This is NO_NAME's scores ---")
print (get_artist_scores(USER_6))						# NO_NAME's score for jcole should be 1, and lana should be 2
USER_5 = get_user_entry(UUID_5)
print ("--- This is kevin's scores ---")
print (get_artist_scores(USER_5))						# kevin's score for jcole should be 2, and lana should be 1
USER_4 = get_user_entry(UUID_4)
print ("--- This is brian's scores ---")
print (get_artist_scores(USER_4))						# brian's score for jcole should be 1, and lana should be 2
USER_1 = get_user_entry(UUID_1)
print ("--- This is jcole's scores ---")
print (get_artist_scores(USER_1))						# jcole's score for himself should be 0, and lana should be 2
USER_2 = get_user_entry(UUID_2)
print ("--- This is lana's scores ---")
print (get_artist_scores(USER_2))						# lana's score for jcole should be 2, and for herself should be 0