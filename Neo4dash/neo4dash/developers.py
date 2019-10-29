from datetime import date

class Developers():
    def __init__(self, nodes, rels):
        self.nodes = nodes
        self.rels = rels

    def list_dev_ids(self):
        dev_nodes = [x for x in self.nodes if x['data']['type'] == 'Developer']
        arr = []

        for x in dev_nodes:
            arr.append(x['data']['id'])

        return arr

    def get_dev_name(self, dev_id):
        dev_nodes = [x for x in self.nodes if x['data']['type'] == 'Developer']

        for x in dev_nodes:
            if x['data']['id'] == dev_id:
                dev_name = x['data']['label']

        return dev_name

    def get_rels_type(self, id, type):
        rel = []

        for x in self.rels:
            if (x['data']['label'] == type):
                if (x['data']['source'] == id):
                    for y in self.nodes:
                        if (y['data']['id'] == x['data']['target']):
                            rel.append(y)

        return rel

    def date_helper(self, frame, id):
        for x in self.rels:
            if (x['data']['target'] == id):
                for y in self.nodes:
                    if (y['data']['id'] == x['data']['source']):
                        if (y['data']['type'] == frame):
                            return y
        return 0

    def get_date_commit(self, commit_id):
        node = self.date_helper('Day', commit_id)
        day = node['data']['label']
        node = self.date_helper('Month', node['data']['id'])
        month = node['data']['label']
        node = self.date_helper('Year', node['data']['id'])
        year = node['data']['label']

        return date(year, month, day)

    def dev_last_active(self, dev_id):
        commits = self.get_rels_type(dev_id, 'Commit')
        recent = 0

        for x in commits:
            y = self.get_date_commit(x['data']['id'])
            if not recent and x:
                recent = y
            elif y > recent:
                recent = y

        return recent

    def print_dev_last(self, dev_id_list):
        entry = ""
        counter = 0

        for dev in dev_id_list:
            ++counter
            dev_name = self.get_dev_name(dev)
            entry += dev_name + ": "
            entry += str(self.dev_last_active(dev))
            print(entry)
            entry = ""

    def dev_get_activity(self, dev_id):

        commits = self.get_rels_type(dev_id, 'Commit')
        #print(commits)
        temp = sorted(commits, key = lambda x: x['data'][''])
