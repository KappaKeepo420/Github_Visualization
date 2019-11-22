from datetime import date
from singleton import Singleton

class Files(metaclass=Singleton):
    def __init__(self, nodes, rels):
        self.nodes = nodes
        self.rels = rels

    def list_file_name(self):
        file_nodes = [x for x in self.nodes if x['data']['type'] == 'File']
        named = []

        for x in file_nodes:
            named.append(x['data']['label'])

        return named
<<<<<<< HEAD
=======


>>>>>>> master
