# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 14:53
# @Author  : Alan
# @Email   : xiezhengwen2013@163.com
# @File    : demo test.py
# @Software: PyCharm


from elasticsearch import  Elasticsearch
import json
es = Elasticsearch()
data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'}
data2 = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
        'date': '2011-12-16'}


'''插入数据'''
# create() 方法需要我们指定 id 字段来唯一标识该条数据
# index() 方法则不需要指定 id 字段，如果不指定 id，会自动生成一个 id
# create() 方法内部其实也是调用了 index() 方法，是对 index() 方法的封装。
# result = es.create(index='news', doc_type='politics', id=1, body=data)
# result2 = es.index(index='news', doc_type='politics', body=data)

'''更新数据'''
# 可以用es.update
# index() 方法可以代替我们完成两个操作，如果数据不存在，那就执行插入操作，如果已经存在，那就执行更新操作
# result = es.index(index='news', doc_type='politics', body=data2)


'''删除数据'''
# result_d = es.delete(index='news', doc_type='politics', id=1)
# print(result_d)

'''查询数据'''
# 安装一个分词插件，这里使用的是 elasticsearch-analysis-ik，GitHub 链接为：https://github.com/medcl/elasticsearch-analysis-ik
# 使用 Elasticsearch 的另一个命令行工具 elasticsearch-plugin 来安装，这里安装的版本是 6.3.2，请确保和 Elasticsearch 的版本对应起来

mapping = {
    'properties':{
        'title':{
            'type': 'text',
            'analyzer': 'ik_max_word',
            'search_analyzer': 'ik_max_word'
        }
    }
}
es.indices.delete(index='news', ignore=[400, 404])
es.indices.create(index='news', ignore=400)
result_q = es.indices.put_mapping(index='news', doc_type='politics', body=mapping)

'''插入新的数据'''
datas = [
    {
        'title': '美国留给伊拉克的是个烂摊子吗',
        'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
        'date': '2011-12-16'
    },
    {
        'title': '公安部：各地校车将享最高路权',
        'url': 'http://www.chinanews.com/gn/2011/12-16/3536077.shtml',
        'date': '2011-12-16'
    },
    {
        'title': '中韩渔警冲突调查：韩警平均每天扣1艘中国渔船',
        'url': 'https://news.qq.com/a/20111216/001044.htm',
        'date': '2011-12-17'
    },
    {
        'title': '中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首',
        'url': 'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
        'date': '2011-12-18'
    }
]
for data in datas:
    es.index(index='news', doc_type='politics', body=data)
result = es.search(index='news', doc_type='politics')
print(result)

'''全文检索'''
dsl = {
    'query':{
        'match':{
            'title':'中国 领事馆'
        }
    }
}
es = Elasticsearch()
result_q2 = es.search(index='news', doc_type='politics', body=dsl)
print(json.dumps(result_q2, indent=2, ensure_ascii=False))