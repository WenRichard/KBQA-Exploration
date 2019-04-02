#!/usr/bin/python                                                                                                                                                                                                                
# coding=utf-8

# File Name: elasticConnect.py
# Author   : john
# company  : foxconn
# Mail     : john.y.ke@mail.foxconn.com 
# Created Time: 2018/12/27 17:35
# Describe : ES数据库处理

from elasticsearch import Elasticsearch
import questionMapping


class ElasticConnect:
    def __init__(self):
        self.elasticConnect = Elasticsearch(hosts=['127.0.0.1'], timeout=50000)  # server connect

    def query_search(self, query):
        return self.elasticConnect.search(index="poem_demo", body=query)

    def get_result(self, num, result):
        values = []
        if (num == 1) | (num == 9) | (num == 5):
            for hit in result['hits']['hits']:
                value = hit['_source']['name']
                values.append(value)
        elif (num == 2) | (num == 8) | (num == 6):
            for hit in result['hits']['hits']:
                value = hit['_source']['author']
                values.append(value)
        elif (num == 7) | (num == 10) | (num == 11):
            for hit in result['hits']['hits']:
                value = hit['_source']['content']
                values.append(value)
        elif (num == 3) | (num == 4):
            for hit in result['hits']['hits']:
                value = hit['_source']['dynasty']
                values.append(value)

        return list(set(values))
