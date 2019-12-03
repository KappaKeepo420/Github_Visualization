from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from singleton import Singleton

class Filter(metaclass=Singleton):
  def __init__(self, nodes, rels):
    self.nodes = nodes
    self.rels = rels
    self.file_nodes = []
    self.full_list = []
    self.rel_list = []

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

  def valid_commits_date(self, date1, date2):
    commits = [x['data']['id'] for x in self.nodes if x['data']['type'] == 'Commit']
    newcommits = []

    for x in commits:
      date = self.get_date_commit(x)
      if date >= date1 and date <= date2:
        newcommits.append(x)

    return newcommits

  def filter_file(self, id_file):
    commit_list = []
    for x in self.rels:
      if x['data']['target'] == id_file:
        if 'Commit' in x['data']['label_concat']:
          commit_list.append(x['data']['source'])

    return commit_list

  def filter_filetype(self, id_filetype):
    commit_list = []
    for x in self.rels:
      if x['data']['source'] == id_filetype:
        for y in self.filter_file(x['data']['target']):
          commit_list.append(y)
    return commit_list

  def filter_developer(self, id_dev):
    commit_list = []
    for x in self.rels:
      if x['data']['source'] == id_dev:
        commit_list.append(x['data']['target'])
    return commit_list

  def gather_commits(self, commit_list):
    for x in commit_list:
      for y in self.nodes: #reverse
        if y['data']['id'] == x:
          self.full_list.append(y)
    for x in commit_list:
      for y in commit_list:
        for z in self.rels:
          if z['data']['source'] == x and z['data']['target'] == y:
              self.rel_list.append(z)

  def gather_dev(self, commit_list):
    for x in commit_list:
      for y in self.rels:
        if y['data']['target'] == x:
          # Neo4j sometimes returns the labels in reverse order
          # see db.py _map_rels
          if "Developer" in y['data']['label_concat']:
            for z in self.nodes:
              if z['data']['id'] == y['data']['source']:
                self.rel_list.append(y)
                if z not in self.full_list:
                  self.full_list.append(z)

  def gather_file_branch(self, commit_list):

    for x in commit_list:
      for y in self.rels:
        if y['data']['source'] == x and "Commit" in y['data']['label_concat']:
          for z in self.nodes:
            if z['data']['id'] == y['data']['target'] and z['data']['type'] != 'Commit':
              self.rel_list.append(y)
              if z not in self.file_nodes:
                self.file_nodes.append(z)
                self.full_list.append(z)

  def gather_filetype(self, commit_list):
    for x in self.file_nodes:
      if x['data']['type'] == 'File':
        for y in self.rels:
          if y['data']['target'] == x['data']['id']:
            for z in self.nodes:
              if z['data']['type'] == 'Filetype':
                if z['data']['id'] == y['data']['source']:
                  self.rel_list.append(y)
                  if z not in self.full_list:
                    self.full_list.append(z)

  def gather_date(self, commit_list):
    day_list = []
    month_list = []

    for x in commit_list:
      for y in self.rels:
        if y['data']['target'] == x and 'Commit' in y['data']['label_concat']:
          for z in self.nodes:
            if z['data']['id'] == y['data']['source']:
              if z['data']['type'] == 'Day':
                self.rel_list.append(y)
                if z not in self.full_list:
                  self.full_list.append(z)
                  day_list.append(z['data']['id'])

    for x in day_list:
      for y in self.rels:
        if y['data']['target'] == x and 'Day' in y['data']['label_concat']:
          for z in self.nodes:
              if z['data']['id'] == y['data']['source']:
                self.rel_list.append(y)
                if z not in self.full_list:
                  self.full_list.append(z)
                  month_list.append(z['data']['id'])

    for x in month_list:
      for y in self.rels:
        if y['data']['target'] == x and 'Year' in y['data']['label_concat']:
          for z in self.nodes:
              if z['data']['id'] == y['data']['source']:
                self.rel_list.append(y)
                if z not in self.full_list:
                  self.full_list.append(z)

  def node_gathering(self, commit_list):

    self.gather_commits(commit_list)
    self.gather_dev(commit_list)
    self.gather_file_branch(commit_list)
    self.gather_filetype(commit_list)
    self.gather_date(commit_list)

  def filter_handler(self, dev_id, file_id, filetype_id, date1, date2):
    dev_list = []
    file_list = []
    filetype_list = []
    date_list = []
    self.full_list = []
    self.rel_list = []
    self.file_nodes = []
    ultralist = []
    result = []

    if dev_id is not None:
      dev_list = self.filter_developer(dev_id)
      ultralist.append(dev_list)
    if file_id is not None:
      file_list = self.filter_file(file_id)
      ultralist.append(file_list)
    if filetype_id is not None:
      filetype_list = self.filter_filetype(filetype_id)
      ultralist.append(filetype_list)
    if date1 is not None:
      if date2 is not None:
        date_list = self.valid_commits_date(date1, date2)
        ultralist.append(date_list)
      else:
        date_list = self.valid_commits_date(date1, date.today())
        ultralist.append(date_list)
    elif date2 is not None:
      date_list = self.valid_commits_date(date(1900,1,1), date2)
      ultralist.append(date_list)

    if len(ultralist) != 0:
      result = ultralist[0]
      for i in range(1, len(ultralist)):
        result = set(result).intersection(ultralist[i])
    else:
      return self.nodes, self.rels

    result = list(result)
    self.node_gathering(result)

    return self.full_list, self.rel_list

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

def developer_to_id(nodes, developer):
  for x in nodes:
    if x['data']['name'] == developer:
      return x['data']['id']
  return None

def file_to_id(nodes, file):
  for x in nodes:
    if x['data']['name'] == file:
      return x['data']['id']
  return None

def filetype_to_id(nodes, filetype):
  for x in nodes:
    if x['data']['name'] == filetype:
      return x['data']['id']
  return None