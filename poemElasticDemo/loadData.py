#!/usr/bin/python                                                                                                                                                           
#coding=utf-8

#File Name: test.py
#Author   : john
#Mail     : john.y.ke@mail.foxconn.com 
#Created Time: Sat 01 Sep 2018 05:38:56 PM CST
#Describe :

import csv
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import sys


# set mapping
def set_mapping(es, index_name="poem_demo", doc_type_name="KBQA"):
    mapping = {
        "properties": {
            "name": {
                "type": "text",
                "analyzer": "ik_smart",
                "search_analyzer": "ik_smart"
            },
			"dynasty": {
				"type": "text",
				"analyzer": "ik_max_word",
				"search_analyzer": "ik_max_word"
			},
            "author": {
                "type": "text",
                "analyzer": "ik_smart",
                "search_analyzer": "ik_smart"
            },
            "content": {
                "type": "text",
                "analyzer": "ik_smart",
                "search_analyzer": "ik_smart"
            }
        }
    }

    es.indices.delete(index=index_name, ignore=[400, 404])
    es.indices.create(index=index_name, ignore=True)
    es.indices.put_mapping(index=index_name, doc_type=doc_type_name, body=mapping)


def set_date(es, index_name="poem_demo", doc_type_name="KBQA"):
    actions = []
    i = 1
    with open('./data/Poem.csv', 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            action = {
                "_index": index_name,
                "_type": doc_type_name,
                "_id": i,
                "_source": {
                    "name": row[0],
					"dynasty": row[1],
                    "author": row[2],
                    "content": row[3],
                }
            }

            i = i + 1

            actions.append(action)

    success, _ = bulk(es, actions, index=index_name, raise_on_error=True)
    print('Performed {} actions'.format(success))


if __name__ == '__main__':
    es = Elasticsearch(hosts=['127.0.0.1:9200'], timeout = 5000)
    set_mapping(es)
    set_date(es)