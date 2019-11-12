def _find_children(nodes, relations, result_nodes, result_relations, node):

    for x in relations:
        if x['data']['source'] == node['data']['id']:
            if x not in result_relations:
                result_relations.append(x)

    target_ids = [x['data']['target'] for x in result_relations]

    target_nodes = []

    for id in target_ids:
        for no in nodes:
            if id == no['data']['id']:
                target_nodes.append(no)

    for target in target_nodes:
        if target not in result_nodes:
            result_nodes.append(target)
            _find_children(nodes, relations, result_nodes, result_relations, target)

def _filter_by(nodes, relations, filter_nodes):
    result_nodes = []
    result_relations = []
    for x in filter_nodes:
        result_nodes.append(x);
        _find_children(nodes, relations, result_nodes, result_relations, x)

    return result_nodes, result_relations

def filter_by_day(nodes, relations, day):
    date_nodes = [x for x in nodes if x['data']['type'] == 'Day']
    dates = [x for x in date_nodes if x['data']['name'] == day]
    return _filter_by(nodes, relations, dates)

def filter_by_month(nodes, relations, month):
    date_nodes = [x for x in nodes if x['data']['type'] == 'Month']
    dates = [x for x in date_nodes if x['data']['name'] == month]
    return _filter_by(nodes, relations, dates)

def filter_by_year(nodes, relations, year):
    date_nodes = [x for x in nodes if x['data']['type'] == 'Year']
    dates = [x for x in date_nodes if x['data']['name'] == year]
    return _filter_by(nodes, relations, dates)

def filter_by_developer(nodes, relations, developer):
    developer_nodes = [x for x in nodes if x['data']['type'] == 'Developer']
    developers = [x for x in date_nodes if x['data']['name'] == developer]
    return _filter_by(nodes, relations, developers) 

# TODO: might not be the best place to put this function
# returns a dictionary with filename as key and amount of commits as value
def commits_per_file(nodes, relations):
    results = dict(); # name, amount

    files = [x for x in nodes if x['data']['type'] == 'File'];
    commits = [x for x in nodes if x['data']['type'] == 'Commit'];

    for f in files:
        results[f['data']['name']] = 0

    for f in files:
        to_file_relations = []
        for r in relations:
            if r['data']['target'] == f['data']['id']:
                to_file_relations.append(r)

        r = [];
        for x in to_file_relations:
            for y in commits:
                if x['data']['source'] == y['data']['id']:
                    results[f['data']['name']] += 1

    return results

