import sys
sys.path.append("./flask/")
from flasklib import *

kill_all()

brian = ("brian", "31", False)
kevin = ("kevin", "11", False)
rahul = ("rahul", "136", False)

chance = ("chance", "1", True)
john_cena = ("john cena", "50", True)
taylor = ("taylor", "22", True)

def make(user):
    create_user_data(user[0], user[1], user[2])

def uuid_of(user):
    return user[1]

def display_all():
    people = get_all_names()
    for person in people:
        person_uuid = person["_id"]
        print(get_name(person_uuid)["name"], person_uuid, get_artist_scores(get_user_entry(person_uuid)))


make(brian)
make(kevin)
make(rahul)
make(chance)
make(john_cena)
make(taylor)

people = get_all_names()
for person in people:
    print(person)

print()

users = get_all_users()
for user in users:
    print(user)

print()

display_all()

print()

make_connection(uuid_of(brian), uuid_of(rahul))
display_all()
print()

make_connection(uuid_of(rahul), uuid_of(taylor))
display_all()

print()

make_connection(uuid_of(taylor), uuid_of(john_cena))
display_all()
