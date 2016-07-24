def make_connection(uuid_1, uuid_2):
	update(uuid_1, uuid_2)
	for neighbor in get_neighbors(uuid_1):
		update(uuid_1, neighbor)
	for neighbor in get_neighbors(uuid_2):
		update(uuid_2, neighbor)
	return None

def update(uuid_1, uuid_2):
	unique_artists = find_artists(uuid_1, uuid_2)
	for artist in unique_artists:
		need_update_tuple = update_required(uuid_1, uuid_2, artist)
		if need_update[0]:
			update(uuid_1, uuid_2, artist, need_update_tuple)
	return None

def find_artists(uuid_1, uuid_2):
	uuid_1_artist_dict = coalesce_to_dict(uuid_1)
	uuid_2_artist_dict = coalesce_to_dict(uuid_2)
	uuid_1_artist_list = [key for key in uuid_1_artist_dict.iterkeys() if uuid_1_artist_dict[key] != MAX_INT]
	uuid_2_artist_list = [key for key in uuid_2_artist_dict.iterkeys() if uuid_2_artist_dict[key] != MAX_INT]
	return list(set(uuid_1_artist_list) | set(uuid_2_artist_list))

def update_required(uuid_1, uuid_2, artist):
	uuid_1_artist_dict = coalesce_to_dict(uuid_1)
	uuid_2_artist_dict = coalesce_to_dict(uuid_2)
	uuid_1_dist = uuid_1_artist_dict[artist]
	uuid_2_dist = uuid_2_artist_dict[artist]
	diff = uuid_1_dist - uuid_2_dist
	shortest_distance = min(uuid_1_dist, uuid_2_dist)
	if abs(diff) > 1:
		return (True, diff, shortest_distance)
	return (False, 0, 0)

def update(uuid_1, uuid_2, artist, need_update_tuple):
	diff = need_update_tuple[1]
	shortest_distance = need_update_tuple[2]
	if diff > 1:
		# index into uuid_1 artist scores, and change the score of the artist to (shortest_distance + 1)
	else:
		# index into uuid_2 artist scores, and change the score of the artist to (shortest_distance + 1)


def coalesce_to_dict(uuid):
	new_dict = {}
	artist_scores = get_distances(uuid)
	for dictionary in artist_scores:
		artist_id = dictionary["_id"]
		artist_distance = dictionary["distance"]
		new_dict[artist_id] = artist_distance
	return new_dict

