from datetime import date
from singleton import Singleton

class Developers(metaclass=Singleton):
    def __init__(self, nodes, rels):
        self.nodes = nodes
        self.rels = rels

    def list_dev_ids(self):
        dev_nodes = [x for x in self.nodes if x['data']['type'] == 'Developer']
        arr = []

        for x in dev_nodes:
            arr.append(x['data']['id'])

        return arr

    def list_dev_name(self):
        dev_nodes = [x for x in self.nodes if x['data']['type'] == 'Developer']
        named = []

        for x in dev_nodes:
            named.append(x['data']['label'])

        return named

    def get_dev_name(self, dev_id):
        dev_nodes = [x for x in self.nodes if x['data']['type'] == 'Developer']

        dev_name = ""
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

    def get_branch_commit(self, commit_id):
        print("omegalul")

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

    def show_developers_activity(self, dev_id_list):
        for dev in dev_id_list:
            print("Developer: " + str(self.get_dev_name(dev)) + '\n')
            print("Total commits: " + str(self._show_dev_activity(dev)) + '\n')

    def _show_dev_activity(self, dev_id):
        commits = self._get_commits(dev_id)
        counter = 0

        if (commits == 0):
            return 0

        for n in commits:
            print("Commit:" + str(n['data']['label']))
            counter += 1
            for x in self.rels:
                if (x['data']['source'] == n['data']['id']):
                    for y in self.nodes:
                        if (y['data']['id'] == x['data']['target']):
                            if (y['data']['type'] == 'Branch'):
                                print("In branch: " + str(y['data']['label']))
                            if (y['data']['type'] == 'File'):
                                print("File: " + str(y['data']['label']))
            print("On: " + str(self.get_date_commit(n['data']['id'])) + '\n')

        return counter

    def _get_commits(self, dev_id):
        commits = []

        for x in self.rels:
            if (x['data']['source'] == dev_id):
                for y in self.nodes:
                    if (y['data']['id'] == x['data']['target']):
                        commits.append(y)

        commits.reverse()

        return commits

    def get_filetype(self, file_id):
        for x in self.rels:
            if (x['data']['target'] == file_id):
                for y in self.nodes:
                    if (y['data']['id'] == x['data']['source']):
                        return y['data']['label']

    def print_dev_last(self, dev_id_list):
        entry = ""
        result = [ ]
        counter = 0
        dev_name = ""

        for dev in dev_id_list:
            ++counter
            dev_name = self.get_dev_name(dev)
            entry += dev_name + ": "
            entry += str(self.dev_last_active(dev))
            entry += "\n"
            result.append(entry)
            print(entry)
            entry = ""

        return result
