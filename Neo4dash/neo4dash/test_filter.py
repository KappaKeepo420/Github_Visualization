import filter
from datetime import datetime, date

def check_list_contain_equal(a, b): 
    if len(a) != len(b): 
        return False

    for i in a: 
        if i not in b: 
            return False

    return True 

def create_node(id, label, type, name):
    d = {}
    d['data'] = {}
    d['data']['id'] = id
    d['data']['label'] = label
    d['data']['type'] = type
    d['data']['name'] = name

    return d

def create_rel(source_node, target_node, id):
    d = {}
    d['data'] = {}
    d['data']['source'] = source_node['data']['id']
    d['data']['target'] = target_node['data']['id']
    d['data']['label'] = str(source_node['data']['type'])
    d['data']['label_concat'] = str(source_node['data']['type']) + str(target_node['data']['type']);
    d['data']['id'] = id 

    return d

def create_fake_db():
    nodes = []
    rels = [] 

    nodes.append(create_node(0, 2018, 'Year', 2018)) 
    nodes.append(create_node(1, 1, 'Month', 1)) 
    nodes.append(create_node(2, 1, 'Day', 1)) 
    nodes.append(create_node(3, 2, 'Day', 2)) 
    nodes.append(create_node(4, 2, 'Month', '2')) 
    nodes.append(create_node(5, 1, 'Day', 1)) 
    nodes.append(create_node(6, 2, 'Day', 2)) 

    nodes.append(create_node( 7, 2019, 'Year', 2019)) 
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
    nodes.append(create_node(22, 'commit_7 ', 'Commit', None)) 
    nodes.append(create_node(23, 'commit_8 ', 'Commit', None)) 
    nodes.append(create_node(24, 'commit_9 ', 'Commit', None)) 

    nodes.append(create_node(25, 'master', 'Branch', 'master')) 

    nodes.append(create_node(26, 'main.py', 'File', 'main.py')) 
    nodes.append(create_node(27, 'function1.py', 'File', 'function1.py'))

    nodes.append(create_node(28, '.py', 'Filetype', '.py')) 

    rels.append(create_rel(nodes[ 0], nodes[ 1], 1 - 1)) # year 2018
    rels.append(create_rel(nodes[ 0], nodes[ 4], 2 - 1))
    rels.append(create_rel(nodes[ 1], nodes[ 2], 3 - 1)) # month 1
    rels.append(create_rel(nodes[ 1], nodes[ 3], 4 - 1))
    rels.append(create_rel(nodes[ 4], nodes[ 5], 5 - 1)) # month 2
    rels.append(create_rel(nodes[ 4], nodes[ 6], 6 - 1))
    rels.append(create_rel(nodes[ 7], nodes[ 8], 7 - 1)) # year 2019
    rels.append(create_rel(nodes[ 7], nodes[11], 8 - 1))
    rels.append(create_rel(nodes[ 8], nodes[ 9], 9 - 1)) # month 1
    rels.append(create_rel(nodes[ 8], nodes[10], 10 - 1))
    rels.append(create_rel(nodes[11], nodes[12], 11 - 1)) # month 2
    rels.append(create_rel(nodes[11], nodes[13], 12 - 1))

   

    rels.append(create_rel(nodes[ 2], nodes[16], 13- 1)); # year 2018; month1; day1
    rels.append(create_rel(nodes[ 3], nodes[17], 14- 1)); # year 2018; month1; day2
    rels.append(create_rel(nodes[ 5], nodes[18], 15- 1)); # year 2018; month2; day1
    rels.append(create_rel(nodes[ 6], nodes[19], 16- 1)); # year 2018; month2; day2

    rels.append(create_rel(nodes[ 9], nodes[20], 17- 1)); # year 2019; month1; day1
    rels.append(create_rel(nodes[10], nodes[21], 18- 1)); # year 2019; month1; day2
    rels.append(create_rel(nodes[12], nodes[22], 19- 1)); # year 2019; month2; day1
    rels.append(create_rel(nodes[13], nodes[23], 20- 1)); # year 2019; month2; day2 
    rels.append(create_rel(nodes[13], nodes[24], 21- 1)); # year 2019; month2; day2 
    
    rels.append(create_rel(nodes[14], nodes[16], 22- 1)) # developer 1 -> commit_
    rels.append(create_rel(nodes[14], nodes[17], 23- 1)) # developer 1 -> commit_
    rels.append(create_rel(nodes[14], nodes[18], 24- 1)) # developer 1 -> commit_
    rels.append(create_rel(nodes[14], nodes[19], 25- 1)) # developer 1 -> commit_
    rels.append(create_rel(nodes[14], nodes[20], 26- 1)) # developer 1 -> commit_
    rels.append(create_rel(nodes[15], nodes[21], 27- 1)) # developer 2 -> commit_
    rels.append(create_rel(nodes[15], nodes[22], 28- 1))
    rels.append(create_rel(nodes[15], nodes[23], 29- 1))
    rels.append(create_rel(nodes[15], nodes[24], 30- 1))

    rels.append(create_rel(nodes[16], nodes[25], 31- 1)) # commit -> master branch
    rels.append(create_rel(nodes[17], nodes[25], 32- 1)) 
    rels.append(create_rel(nodes[18], nodes[25], 33- 1)) 
    rels.append(create_rel(nodes[19], nodes[25], 34- 1)) 
    rels.append(create_rel(nodes[20], nodes[25], 35- 1)) 
    rels.append(create_rel(nodes[21], nodes[25], 36- 1)) 
    rels.append(create_rel(nodes[22], nodes[25], 37- 1))
    rels.append(create_rel(nodes[23], nodes[25], 38- 1))
    rels.append(create_rel(nodes[24], nodes[25], 39- 1))

    rels.append(create_rel(nodes[16], nodes[26], 40- 1)) # commit_ -> main.py
    rels.append(create_rel(nodes[17], nodes[26], 41- 1)) # commit_ -> main.py
    rels.append(create_rel(nodes[18], nodes[26], 42- 1)) # commit_ -> main.py
    rels.append(create_rel(nodes[19], nodes[26], 43- 1)) # commit_ -> main.py
    rels.append(create_rel(nodes[20], nodes[26], 44- 1)) # commit_ -> main.py
    rels.append(create_rel(nodes[21], nodes[26], 45- 1)) # commit_ -> main.py
    rels.append(create_rel(nodes[22], nodes[26], 46- 1)) # commit_ -> main.py
    rels.append(create_rel(nodes[23], nodes[26], 47- 1)) # commit_ -> main.py
    rels.append(create_rel(nodes[24], nodes[26], 48- 1)) # commit_ -> main.py
    rels.append(create_rel(nodes[25], nodes[26], 49- 1)) # commit_ -> main.py
    rels.append(create_rel(nodes[16], nodes[27], 50- 1)) # commit_ -> function1.py

    rels.append(create_rel(nodes[26], nodes[28], 51- 1)) # main.py -> .py
    rels.append(create_rel(nodes[27], nodes[28], 52- 1)) # function.py -> .py 

    return nodes, rels


def result_developer_1():
    nodes, rels = create_fake_db() 

    # manual filtering 
    nodes.pop(28)
    nodes.pop(24)
    nodes.pop(23)
    nodes.pop(22)
    nodes.pop(21)
    nodes.pop(15)
    nodes.pop(13)
    nodes.pop(12)
    nodes.pop(11) 
    nodes.pop(10) 
    #rels.pop(51) #NOTE: BUG, shouldn't remove this
    #rels.pop(50) #NOTE: BUG, shouldn't remove this
    rels.pop(48)
    rels.pop(47)
    rels.pop(46)
    rels.pop(45)
    rels.pop(44)
    rels.pop(38)
    rels.pop(37)
    rels.pop(36)
    rels.pop(35)
    rels.pop(29)
    rels.pop(28)
    rels.pop(27)
    rels.pop(26)
    rels.pop(20)
    rels.pop(19)
    rels.pop(18)
    rels.pop(17)
    rels.pop(11)
    rels.pop(10)
    rels.pop(9)
    rels.pop(7)

    return nodes, rels    

def result_date_1():
    nodes, rels = create_fake_db() 

    nodes.pop(28); 
    nodes.pop(27);
    nodes.pop(19);
    nodes.pop(18);
    nodes.pop(17);
    nodes.pop(16);
    nodes.pop(6);
    nodes.pop(5);
    nodes.pop(4);
    nodes.pop(3);
    nodes.pop(2);
    nodes.pop(1);
    nodes.pop(0); 
    rels.pop(51); #NOTE: BUG
    rels.pop(50); #NOTE: BUG
    rels.pop(49);
    rels.pop(48);
    rels.pop(42);
    rels.pop(41);
    rels.pop(40);
    rels.pop(39);
    rels.pop(33);
    rels.pop(32);
    rels.pop(31);
    rels.pop(30);
    rels.pop(24);
    rels.pop(23);
    rels.pop(22);
    rels.pop(21);
    rels.pop(15);
    rels.pop(14);
    rels.pop(13);
    rels.pop(12);
    rels.pop(5);
    rels.pop(4);
    rels.pop(3);
    rels.pop(2);
    rels.pop(1);
    rels.pop(0);
    return nodes, rels

def result_date_2():
    nodes, rels = create_fake_db() 

    nodes.pop(28);
    nodes.pop(24);
    nodes.pop(23);
    nodes.pop(22);
    nodes.pop(21);
    nodes.pop(20);
    nodes.pop(15);
    nodes.pop(13);
    nodes.pop(12);
    nodes.pop(11);
    nodes.pop(10);
    nodes.pop(9);
    nodes.pop(8);
    nodes.pop(7); 
    rels.pop(51); #NOTE: BUG
    rels.pop(50); #NOTE: BUG
    rels.pop(48);
    rels.pop(47);
    rels.pop(46);
    rels.pop(45);
    rels.pop(44);
    rels.pop(43);
    rels.pop(38);
    rels.pop(37);
    rels.pop(36);
    rels.pop(35);
    rels.pop(34);
    rels.pop(29);
    rels.pop(28);
    rels.pop(27);
    rels.pop(26);
    rels.pop(25);
    rels.pop(20);
    rels.pop(19);
    rels.pop(18);
    rels.pop(17);
    rels.pop(16);
    rels.pop(11);
    rels.pop(10);
    rels.pop(9);
    rels.pop(8);
    rels.pop(7);
    rels.pop(6); 

    return nodes, rels 

def test_filter(): 
    nodes, rels = create_fake_db()

    try:
        print("checking no filter")
        ft = filter.Filter(nodes, rels) 
        n, r = ft.filter_handler(None, None, None, None, None) 
        assert(check_list_contain_equal(nodes, n));
        assert(check_list_contain_equal(rels, r)); 
        print("checking no filter done")
    except AssertionError:
        print("checking no filter failed")

    # check developer
    try:
        print("checking developer")
        n, r = ft.filter_handler(filter.developer_to_id(nodes, 'Developer 1'), None, None, None, None) 
        xn, xr = result_developer_1() 
        assert(check_list_contain_equal(n, xn));
        assert(check_list_contain_equal(r, xr)); 
        print("checking developer done")
    except AssertionError:
        print("checking developer failed")

    try:
        print("checking date 1")
        n, r = ft.filter_handler(None, None, None, datetime.strptime("31-12-2018", '%d-%m-%Y').date(), None) 
        xn, xr = result_date_1() 
        assert(check_list_contain_equal(n, xn));
        assert(check_list_contain_equal(r, xr)); 
        print("checking date 1 done")
    except AssertionError:
        print("checking date 1 failed")

    try:
        print("checking date 2")
        n, r = ft.filter_handler(None, None, None, None, datetime.strptime("31-12-2018", '%d-%m-%Y').date()) 
        xn, xr = result_date_2() 
        assert(check_list_contain_equal(n, xn));
        assert(check_list_contain_equal(r, xr)); 
        print("checking date 2 done")
    except AssertionError:
        print("checking date 2 failed")

def main(): 
    print('begin test_filter')
    test_filter() 
    print('end test_filter')

if __name__ == '__main__':
    main();
