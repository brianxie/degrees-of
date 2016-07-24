import requests

root_address = "http://10.123.147.139:5000/"

create_user_data_address = root_address + "createuserdata"
create_user_data_payload_1 = {"name": "lana", "uuid": 1, "is_artist": True}
create_user_data_payload_2 = {"name": "kanye", "uuid": 2, "is_artist": True}
create_user_data_payload_3 = {"name": "rahul", "uuid": 3, "is_artist": False}

r1 = requests.post(create_user_data_address, create_user_data_payload_1)
print(r1.text)
r2 = requests.post(create_user_data_address, create_user_data_payload_2)
print(r2.text)
r3 = requests.post(create_user_data_address, create_user_data_payload_3)
print(r3.text)

print()

get_user_entry_address = root_address + "getuserentry"
get_user_entry_payload_1 = {"uuid": 1}
get_user_entry_payload_2 = {"uuid": 2}
get_user_entry_payload_3 = {"uuid": 3}

r1 = requests.get(get_user_entry_address, get_user_entry_payload_1)
print(r1.text)
r2 = requests.get(get_user_entry_address, get_user_entry_payload_2)
print(r2.text)
r3 = requests.get(get_user_entry_address, get_user_entry_payload_3)
print(r3.text)

print()

get_artist_scores_address = root_address + "getartistscores"
get_artist_scores_payload_1 = {"uuid": 1}
get_artist_scores_payload_2 = {"uuid": 2}
get_artist_scores_payload_3 = {"uuid": 3}

r1 = requests.get(get_artist_scores_address, get_artist_scores_payload_1)
print(r1.text)
r2 = requests.get(get_artist_scores_address, get_artist_scores_payload_2)
print(r2.text)
r3 = requests.get(get_artist_scores_address, get_artist_scores_payload_3)
print(r3.text)

print()

get_name_address = root_address + "getname"
get_name_payload_1 = {"uuid": 1}
get_name_payload_2 = {"uuid": 2}
get_name_payload_3 = {"uuid": 3}

r1 = requests.get(get_name_address, get_name_payload_1)
print(r1.text)
r2 = requests.get(get_name_address, get_name_payload_2)
print(r2.text)
r3 = requests.get(get_name_address, get_name_payload_3)
print(r3.text)

print()

make_connection_address = root_address + "makeconnection"
make_connection_payload_1 = {"uuid_1": 1, "uuid_2": 2}

r1 = requests.post(make_connection_address, make_connection_payload_1)
print(r1.text)

r1 = requests.get(get_artist_scores_address, get_artist_scores_payload_1)
print(r1.text)
r2 = requests.get(get_artist_scores_address, get_artist_scores_payload_2)
print(r2.text)
