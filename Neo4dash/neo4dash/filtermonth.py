def filter_by_month(self, month):
    nodes, rels = self.get_all_data(merge = False)

    month_nodes = [x for x in nodes if x['data']['type'] == 'Month']

    month = [x for x in month_nodes if x['data']['name'] == month]

    arr = []


    for x in rels:
        for y in nodes:
            for z in month:
                if x['data']['source'] == z['data']['id']:
                    if x['data']['target'] == y['data']['id']:
                        arr.append(y)


    return arr, rels
