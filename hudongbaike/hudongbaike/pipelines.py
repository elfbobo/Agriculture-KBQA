# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings  # 导入seetings配置
import pymysql


class HudongbaikePipeline(object):

    def __init__(self):
        settings = get_project_settings()  # 获取settings配置，设置需要的信息

        dbparams = dict(
            host=settings['MYSQL_HOST'],  # 读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql, self._sql2, self._sql3, = None, None, None

    def process_item(self, item, spider):

        # 基本属性
        self.Attr_info_insert(item)
        # 基本简介
        self.Base_info_insert(item)
        # 详细信息
        self.QA_info_insert(item)
        return item

    def Attr_info_insert(self, item):
        for key, value in item["attr_data"].items():
            _sql = '''insert into Atterinfo(id, name, attr_key,attr_value) values(%s,%s,%s,%s)'''
            self.cursor.execute(_sql, (item['id'], item['name'], key, value))
            self.conn.commit()

    def Base_info_insert(self, item):
        _sql2 = '''insert into Baseinfo(id, name, intro) values(%s,%s,%s)'''
        self.cursor.execute(_sql2, (item['id'], item['name'], item['intro']))
        self.conn.commit()

    def QA_info_insert(self, item):
        for question, answer in item['base_info'].items():
            _sql3 = '''insert into QAdata(id, name, question, answer) values(%s,%s,%s,%s)'''
            self.cursor.execute(_sql3, (item['id'], item['name'], question, answer))
            self.conn.commit()
