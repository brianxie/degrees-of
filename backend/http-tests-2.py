import requests

root_address = "http://10.123.147.139:5000/"

create_user_data_address = root_address + "createuserdata"
create_user_data_payload_1 = {"name": "jcole", "uuid": 1, "is_artist": True}
create_user_data_payload_2 = {"name": "lana", "uuid": 2, "is_artist": True}
create_user_data_payload_3 = {"name": "rahul", "uuid": 3, "is_artist": False}
create_user_data_payload_4 = {"name": "brian", "uuid": 4, "is_artist": False}
create_user_data_payload_5 = {"name": "kevin", "uuid": 5, "is_artist": False}
create_user_data_payload_6 = {"name": "claremont", "uuid": 6, "is_artist": False}

r1 = requests.post(create_user_data_address, create_user_data_payload_1)
print(r1.text)
r2 = requests.post(create_user_data_address, create_user_data_payload_2)
print(r2.text)
r3 = requests.post(create_user_data_address, create_user_data_payload_3)
print(r3.text)
r4 = requests.post(create_user_data_address, create_user_data_payload_4)
print(r4.text)
r5 = requests.post(create_user_data_address, create_user_data_payload_5)
print(r5.text)
r6 = requests.post(create_user_data_address, create_user_data_payload_6)
print(r6.text)

print()

get_user_entry_address = root_address + "getuserentry"
get_user_entry_payload_1 = {"uuid": 1}
get_user_entry_payload_2 = {"uuid": 2}
get_user_entry_payload_3 = {"uuid": 3}
get_user_entry_payload_4 = {"uuid": 4}
get_user_entry_payload_5 = {"uuid": 5}
get_user_entry_payload_6 = {"uuid": 6}


r1 = requests.get(get_user_entry_address, get_user_entry_payload_1)
print(r1.text)
r2 = requests.get(get_user_entry_address, get_user_entry_payload_2)
print(r2.text)
r3 = requests.get(get_user_entry_address, get_user_entry_payload_3)
print(r3.text)
r4 = requests.get(get_user_entry_address, get_user_entry_payload_4)
print(r4.text)
r5 = requests.get(get_user_entry_address, get_user_entry_payload_5)
print(r5.text)
r6 = requests.get(get_user_entry_address, get_user_entry_payload_6)
print(r6.text)

print()

get_artist_scores_address = root_address + "getartistscores"
get_artist_scores_payload_1 = {"uuid": 1}
get_artist_scores_payload_2 = {"uuid": 2}
get_artist_scores_payload_3 = {"uuid": 3}
get_artist_scores_payload_4 = {"uuid": 4}
get_artist_scores_payload_5 = {"uuid": 5}
get_artist_scores_payload_6 = {"uuid": 6}

r1 = requests.get(get_artist_scores_address, get_artist_scores_payload_1)
print(r1.text)
r2 = requests.get(get_artist_scores_address, get_artist_scores_payload_2)
print(r2.text)
r3 = requests.get(get_artist_scores_address, get_artist_scores_payload_3)
print(r3.text)
r4 = requests.get(get_artist_scores_address, get_artist_scores_payload_4)
print(r4.text)
r5 = requests.get(get_artist_scores_address, get_artist_scores_payload_5)
print(r5.text)
r6 = requests.get(get_artist_scores_address, get_artist_scores_payload_6)
print(r6.text)

print()

get_name_address = root_address + "getname"
get_name_payload_1 = {"uuid": 1}
get_name_payload_2 = {"uuid": 2}
get_name_payload_3 = {"uuid": 3}
get_name_payload_4 = {"uuid": 4}
get_name_payload_5 = {"uuid": 5}
get_name_payload_6 = {"uuid": 6}

r1 = requests.get(get_name_address, get_name_payload_1)
print(r1.text)
r2 = requests.get(get_name_address, get_name_payload_2)
print(r2.text)
r3 = requests.get(get_name_address, get_name_payload_3)
print(r3.text)
r4 = requests.get(get_name_address, get_name_payload_4)
print(r4.text)
r5 = requests.get(get_name_address, get_name_payload_5)
print(r5.text)
r6 = requests.get(get_name_address, get_name_payload_6)
print(r6.text)

print()

first = requests.get(get_user_entry_address, get_name_payload_3)
print(first.text)
second = requests.get(get_user_entry_address, get_name_payload_4)
print(second.text)

print()

make_connection_address = root_address + "makeconnection"
make_connection_payload_3 = {"uuid_1": 3, "uuid_2": 4}

r3 = requests.post(make_connection_address, make_connection_payload_3)
print(r3.text)

print()

r3 = requests.get(get_artist_scores_address, get_artist_scores_payload_3)
print(r3.text)
r4 = requests.get(get_artist_scores_address, get_artist_scores_payload_4)
print(r4.text)

print()

kill_all_address = root_address + "killall"
rkill = requests.post(kill_all_address, {})
print(rkill.text)