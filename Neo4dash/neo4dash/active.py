from datetime import date

def list_dev_ids(nodes, rels):
	dev_nodes = [x for x in nodes if x['data']['type'] == 'Developer']
	arr = []

	for x in dev_nodes:
	    arr.append(x['data']['id'])

	return arr

def get_dev_name(nodes, rels, dev_id):
	dev_nodes = [x for x in nodes if x['data']['type'] == 'Developer']

	for x in dev_nodes:
	    if x['data']['id'] == dev_id:
	        dev_name = x['data']['label']

	return dev_name


def get_rels_type(nodes, rels, id, type):
	rel = []

	for x in rels:
	    if (x['data']['label'] == type):
	        if (x['data']['source'] == id):
	            for y in nodes:
	                if (y['data']['id'] == x['data']['target']):
	                    rel.append(y)

	return rel

def date_helper(nodes, rels, frame, id):
	for x in rels:
	    if (x['data']['target'] == id):
	        for y in nodes:
	            if (y['data']['id'] == x['data']['source']):
	                if (y['data']['type'] == frame):
	                    return y
	return 0

def get_date_commit(nodes, rels, commit_id):
	node = date_helper(nodes, rels, 'Day', commit_id)
	day = node['data']['label']
	node = date_helper(nodes, rels, 'Month', node['data']['id'])
	month = node['data']['label']
	node = date_helper(nodes, rels, 'Year', node['data']['id'])
	year = node['data']['label']

	return date(year, month, day)


def dev_last_active(nodes, rels, dev_id):
	commits = get_rels_type(nodes, rels, dev_id, 'Commit')
	recent = 0

	for x in commits:
	    y = get_date_commit(nodes, rels, x['data']['id'])
	    if not recent and x:
	        recent = y
	    elif y > recent:
	        recent = y

	return recent


def list_dev_last(nodes, rels, dev_id_list):
		entry = ""
		counter = 0

		for dev in dev_id_list:
				counter += 1
				dev_name = get_dev_name(nodes, rels, dev)
				entry += dev_name + ": "
				entry += str(dev_last_active(nodes, rels, dev))
				print(entry)
				entry = ""