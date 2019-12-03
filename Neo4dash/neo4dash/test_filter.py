import filter

def create_node(id, label, type, name):
    d = {}
    d['data'] = {}
    d['data']['2'] = id
    d['data']['label'] = label
    d['data']['type'] = type
    d['data']['name'] = name

    return d

def create_rel(source_node, target_node):
    d = {}
    d['data'] = {}
    d['data']['source'] = source_node['data']['id']
    d['data']['target'] = target_node['data']['id']
    d['data']['label_concat'] = source_node['data']['label'] + target_node['data']['label']; # TODO: maybe this is the otherway around
    d['data']['id'] = 0 #TODO: id not set

    return d

def test_empty():
    # TODO: add more filter arguments

    nodes = []
    rels = []

    ft = filter.Filter(nodes, rels)

    n, r = ft.filter_handler(None, None, None, None, None)

    assert nodes.sort() == n.sort()
    assert rels.sort() == r.sort()

def test_developer():
    # TODO: implement 
    nodes = []
    rels = [] 

    nodes.append(create_node(0, 2019, 'Year', 2019)) 
    nodes.append(create_node(1, 1, 'Month', 1)) 
    nodes.append(create_node(2, 1, 'Day', 1)) 
    nodes.append(create_node(3, 2, 'Day', 2)) 
    nodes.append(create_node(4, 2, 'Month', '2')) 
    nodes.append(create_node(5, 1, 'Day', 1)) 
    nodes.append(create_node(6, 2, 'Day', 2)) 

    nodes.append(create_node( 7, 2018, 'Year', 2018)) 
    nodes.append(create_node( 8, 1, 'Month', 1)) 
    nodes.append(create_node( 9, 1, 'Day', 1)) 
    nodes.append(create_node(10, 2, 'Day', 2)) 
    nodes.append(create_node(11, 2, 'Month', 2)) 
    nodes.append(create_node(12, 1, 'Day', 1)) 
    nodes.append(create_node(13, 2, 'Day', 2))


    nodes.append(create_node(14, 'Developer 1', 'Developer', 'Developer 1')) 
    nodes.append(create_node(15, 'Developer 2', 'Developer', 'Developer 2'))


    nodes.append(create_node(16, 'commit_1 ', 'Commit', None)) 
    nodes.append(create_node(17, 'commit_2 ', 'Commit', None)) 
    nodes.append(create_node(18, 'commit_3 ', 'Commit', None)) 
    nodes.append(create_node(19, 'commit_4 ', 'Commit', None)) 
    nodes.append(create_node(20, 'commit_5 ', 'Commit', None)) 
    nodes.append(create_node(21, 'commit_6 ', 'Commit', None)) 
    nodes.append(create_node(22, 'commit_7 ', 'Commit', None) ) 
    nodes.append(create_node(23, 'commit_8 ', 'Commit', None)) 
    nodes.append(create_node(24, 'commit_9 ', 'Commit', None))


    nodes.append(create_node(25, 'master', 'Branch', 'master')) 

    nodes.append(create_node(26, 'main.py', 'File', 'main.py') 
    nodes.append(create_node(27, 'function1.py', 'File', 'main.py') 

    nodes.append(create_node(28, '.py', 'Filetype', '.py')

    rels.append(create_rel(nodes[ 0], nodes[ 1])) # year 2018
    rels.append(create_rel(nodes[ 0], nodes[ 4]))
    rels.append(create_rel(nodes[ 1], nodes[ 2])) # month 1
    rels.append(create_rel(nodes[ 1], nodes[ 3]))
    rels.append(create_rel(nodes[ 4], nodes[ 5])) # month 2
    rels.append(create_rel(nodes[ 4], nodes[ 6]))
    rels.append(create_rel(nodes[ 7], nodes[ 8])) # year 2019
    rels.append(create_rel(nodes[ 7], nodes[11]))
    rels.append(create_rel(nodes[ ], nodes[])) # month 1
    rels.append(create_rel(nodes[ ], nodes[]))
    rels.append(create_rel(nodes[ ], nodes[])) # month 2
    rels.append(create_rel(nodes[ ], nodes[]))




    ft = filter.Filter(nodes, rels)

    n, r = ft.filter_handler(None, None, None, None, None)

    assert nodes.sort() == n.sort()
    assert rels.sort() == r.sort()





def test_file():
    # TODO: implement
    print('not implemented')

def test_filetype():
    # TODO: implement
    print('not implemented')

def test_dates():
    # TODO: implement
    print('not implemented')

def test_various_combinations():
    # TODO: implement
    print('not implemented')

def test_developer_to_33():
    # TODO: implement
    print('not implemented')

def test_file_to_34():
    # TODO: implement
    print('not implemented')

def test_filetype_to_35():
    # TODO: implement
    print('not implemented')


def test_filter():
    test_empty()
    test_developer()
    test_file()
    test_filetype()
    test_dates()
    test_various_combinations()
    test_developer_to_36()
    test_file_to_37()
    test_filetype_to_38()

def main(): 
    print('begin test_filter')
    test_filter() 
    print('end test_filter')

if __name__ == '__main__':
    main();
