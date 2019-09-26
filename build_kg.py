#!/usr/bin/env python3
# coding: utf-8


import json
import os
import pandas as pd
from py2neo import Graph, Node, Relationship, NodeMatcher


class GoodsKg:
    def __init__(self):
        cur = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        self.data_path = os.path.join(cur, 'data/goods_info.json')
        self.g = Graph(
            host="127.0.0.1",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
            http_port=7474,  # neo4j 服务器监听的端口号
            user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
            password="")

    # 获取数据
    def read_data(self):
        rels_goods = []
        rels_brand = []
        goods_attrdict = {}
        concept_goods = set()
        concept_brand = set()
        count = 0
        for line in open(self.data_path):
            count += 1
            print(count)
            line = line.strip()
            data = json.loads(line)
            first_class = data['fisrt_class'].replace("'", '')
            second_class = data['second_class'].replace("'", '')
            third_class = data['third_class'].replace("'", '')
            attr = data['attrs']
            concept_goods.add(first_class)
            concept_goods.add(second_class)
            concept_goods.add(third_class)
            rels_goods.append('@'.join([second_class, 'is_a', '属于', first_class]))
            rels_goods.append('@'.join([third_class, 'is_a', '属于', second_class]))

            if attr and '品牌' in attr:
                brands = attr['品牌'].split(';')
                for brand in brands:
                    brand = brand.replace("'", '')
                    concept_brand.add(brand)
                    rels_brand.append('@'.join([brand, 'sales', '销售', third_class]))

            goods_attrdict[third_class] = {name: value for name, value in attr.items() if name != '品牌'}

        return concept_brand, concept_goods, rels_goods, rels_brand

    # 建立节点
    def create_node(self, label, nodes):
        pairs = []
        bulk_size = 1000
        batch = 0
        bulk = 0
        batch_all = len(nodes) // bulk_size
        print(batch_all)
        for node_name in nodes:
            sql = """CREATE(:%s {name:'%s'})""" % (label, node_name)
            pairs.append(sql)
            bulk += 1
            if bulk % bulk_size == 0 or bulk == batch_all + 1:
                sqls = '\n'.join(pairs)
                self.g.run(sqls)
                batch += 1
                print(batch * bulk_size, '/', len(nodes), 'finished')
                pairs = []
        return

    # 建立关系
    def create_edges(self, rels, start_type, end_type):
        batch = 0
        count = 0
        for rel in set(rels):
            count += 1
            rel = rel.split('@')
            start_name = rel[0]
            end_name = rel[3]
            rel_type = rel[1]
            rel_name = rel[2]
            sql = 'match (m:%s), (n:%s) where m.name = "%s" and n.name = "%s" create (m)-[:%s{name:"%s"}]->(n)' % (
                start_type, end_type, start_name, end_name, rel_type, rel_name)
            try:
                self.g.run(sql)
            except Exception as e:
                print(e)
            if count % 10 == 0:
                print(count)

        return

    # 构建图
    def start(self):
        concept_brand, concept_goods, rels_goods, rels_brand = self.read_data()
        # print('creating nodes....')
        # self.create_node('Product', concept_goods)
        # self.create_node('Brand', concept_brand)
        # print('creating edges....')
        # self.create_edges(rels_goods, 'Product', 'Product')
        self.create_edges(rels_brand, 'Brand', 'Product')
        return


if __name__ == '__main__':
    handler = GoodsKg()
    graph = handler.g
    tx = graph.begin()



    # a = Node('Person', name='A')
    # # b = Node('Person', name='B')
    # # c = Node('Person', name='c')
    # # d = Node('Person', name='d')
    # e = Node('Person', name='Bas')
    # # r1 = Relationship(a,'KNOWS', b)
    # # r2 = Relationship(c,'KNOWS', d)
    # # r3 = Relationship(a,'KNOWS', c)
    # r4 = Relationship(a, 'KNOWS', e)
    # tx.merge(r4, primary_label='Person',primary_key='name')
    # tx.commit()



    # s = a | b | c | r1 | r2 | r3
    # graph.create(s)

    # b.setdefault('location', '北京')
    # b['location'] = '上海'
    # b.setdefault('location', '北京')
    # print(b)
    # data = {
    #     'name': 'Amy',
    #     'age': 21
    # }
    # a.update(data)
    # handler.g.create(a)
    # a['sex'] = 8000
    # handler.g.push(a)
    # print(a)
    # handler.run()
    # a["age"] = 10
    # handler.g.push(a)

    # 查询
    matcher = NodeMatcher(graph)
    # # node = matcher.match("Ticket")#.where("_.name = 'A'")
    # # # handler.g.delete(node)
    # # print(list(node))
    # # for n in node.__iter__():
    # #     handler.g.delete(n)
    # # a = graph.run('MATCH (p:Person) return p').data()
    a = matcher.match("Person").where("_.name =~ 'B.*?'")
    print(list(a))
    # graph.match_one(r_type='KNOWS')