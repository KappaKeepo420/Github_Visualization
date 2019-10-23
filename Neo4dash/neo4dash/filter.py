def _find_children(nodes, relations, node):
    result_relations = []
    for x in relations:
        if x['data']['source'] == node['data']['id']:
            result_relations.append(x)

    target_ids = [x['data']['target'] for x in result_relations]
    result_nodes = []

    target_nodes = []
    for id in target_ids:
        for no in nodes:
            if id == no['data']['id']:
                target_nodes.append(no)

    for target in target_nodes:
        result_nodes.append(target)
        n, r = _find_children(nodes, relations, target)
        result_nodes += n
        result_relations += r

    return result_nodes, result_relations

def _filter_by(nodes, relations, filter_nodes):
    result_nodes = []
    result_relations = []
    for x in filter_nodes:
        result_nodes.append(x);
        n, r = _find_children(nodes, relations, x)
        result_nodes += n
        result_relations += r

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

    return result_nodes, result_relations