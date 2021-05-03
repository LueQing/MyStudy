from py2neo import Graph,Node,Relationship,NodeMatcher
import py2neo
import csv


label = '知识'

g=Graph('http://localhost:7474', user='neo4j', password='2333')

#g.run('match (n) detach delete n') #删除所有数据

with open('./知识.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for item in reader:
        if reader.line_num == 1:
            continue
        print('当前行数', reader.line_num, '当前内容', item)

        start_node=Node(label, name=item[0])
        print(g)

        end_node=Node(label, name=item[1])


        relation=Relationship(start_node, item[2], end_node)

        if (item[3] != ''):
            plus = item[3].split(':')
            print(plus)
            if (plus[0] == '1'):
                start_node[plus[1]] = plus[2]
            else:
                end_node[plus[1]] = plus[2]
        
        #g.merge(start_node, label, 'name')
        #g.merge(end_node, label, 'name')
        g.merge(relation, label, 'name')
