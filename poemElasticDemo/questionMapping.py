#!/usr/bin/python                                                                                                                                                                                                                
# coding=utf-8

# File Name: questionMapping.py
# Author   : john
# company  : foxconn
# Mail     : john.y.ke@mail.foxconn.com 
# Created Time: 2018/12/25 10:51
# Describe :

from refo import finditer, Predicate, Star, Any   # 正则表达式库
import re


class W(Predicate):
    def __init__(self, token=".*", pos=".*"):
        self.token = re.compile(token + "$")
        self.pos = re.compile(pos + "$")
        # match继承父类W 的属性
        super(W, self).__init__(self.match)

    def match(self, word):
        m1 = self.token.match(word.token)
        m2 = self.pos.match(word.pos)
        print('m1, m2:')
        print(m1, m2)
        return m1 and m2


class Rule(object):
    def __init__(self, condition_num, condition=None, action=None):
        assert condition and action
        self.condition = condition
        self.action = action
        self.condition_num = condition_num

    def apply(self, sentence):
        matches = []
        # finditer返回一个可迭代对象
        for m in finditer(self.condition, sentence):
            # i,j 为字符串的起始位置
            i, j = m.span()
            matches.extend(sentence[i:j])
        print('matchs:')
        print(self.action(matches), self.condition_num)
        return self.action(matches), self.condition_num


# TODO 定义关键词
pos_poet = "nr"   # 诗人名
pos_poem = "nz"  # 诗词名
pos_dynasty = "nt"    # 朝代
pos_verse = "x"  # 诗句

poet_entity = (W(pos=pos_poet))
poem_entity = (W(pos=pos_poem))
dynasty_entity = (W(pos=pos_dynasty))
verse_entity = (W(pos=pos_verse))

poem = (W("诗") | W("词") | W("古诗") | W("诗词") | W("文章") | W("作品") | W("诗歌"))
poet = (W("诗人") | W("作者") | W("谁"))
dynasty = (W("朝代") | W("年代") | W("时候") | W("时间") | W("时代"))
content = (W("内容"))
born = (W("出自"))
next_verse = (W("下一句") | W("下句"))
prev_verse = (W("上一句") | W("上句"))


'''1. 某个诗人写了哪些诗
2.某首诗是谁写的
3.哪个诗人是哪个朝代的
4.哪首诗是哪个朝代的
5.哪个朝代有哪些诗
6.哪个朝代有哪些诗人
8.诗歌具体内容
9.诗句是哪个诗人写的
10.诗句出自哪首诗
11.上一句
12.下一句'''
class Question:
    def __init__(self):
        pass

    @staticmethod
    def poet_search_question(word_objects):  # 诗人查询
        query = None
        for w in word_objects:
            if w.pos == pos_poet:
                query = {"query": {"bool": {"must": [{"query_string": {"default_field": "author", "query": w.token}}]}}, "size":100}
                break

        return query

    @staticmethod
    def poem_search_question(word_objects):  # 诗词名查询
        query = None
        for w in word_objects:
            if w.pos == pos_poem:
                query = {"query": {"bool": {"must": [{"query_string": {"default_field": "name", "query": w.token}}]}}, "size": 5}
                break

        return query

    @staticmethod
    def content_search_question(word_objects):  # 诗词内容查询
        query = None
        for w in word_objects:
            if w.pos == pos_verse:
                query = {"query": {"bool": {"must": [{"query_string": {"default_field": "content", "query": w.token}}]}}, "size": 5}
                break

        return query

    @staticmethod
    def dynasty_search_question(word_objects):  # 朝代查询
        query = None
        for w in word_objects:
            if w.pos == pos_dynasty:
                query = {
                    "query": {"bool": {"must": [{"query_string": {"default_field": "dynasty", "query": w.token}}]}}, "size": 100}
                break

        return query


rules = [
    Rule(condition_num=1, condition=((poet_entity + Star(Any(), greedy=False) + poem + Star(Any(), greedy=False)) | (poem + Star(Any(), greedy=False) + poet_entity + Star(Any(), greedy=False))), action=Question.poet_search_question),
    Rule(condition_num=2, condition=((poem_entity + Star(Any(), greedy=False) + poet + Star(Any(), greedy=False)) | (poet + Star(Any(), greedy=False) + poem_entity + Star(Any(), greedy=False))), action=Question.poem_search_question),
    Rule(condition_num=3, condition=(poet_entity + Star(Any(), greedy=False) + dynasty + Star(Any(), greedy=False)), action=Question.poet_search_question),
    Rule(condition_num=4, condition=(poem_entity + Star(Any(), greedy=False) + dynasty + Star(Any(), greedy=False)), action=Question.poem_search_question),
    Rule(condition_num=5, condition=((dynasty_entity + Star(Any(), greedy=False) + poem + Star(Any(), greedy=False)) | (poem + Star(Any(), greedy=False) + dynasty_entity + Star(Any(), greedy=False))), action=Question.dynasty_search_question),
    Rule(condition_num=6, condition=((dynasty_entity + Star(Any(), greedy=False) + poet + Star(Any(), greedy=False)) | (poet + Star(Any(), greedy=False) + dynasty_entity + Star(Any(), greedy=False))), action=Question.dynasty_search_question),
    Rule(condition_num=7, condition=(poem_entity + Star(Any(), greedy=False)), action=Question.poem_search_question),
    Rule(condition_num=8, condition=((verse_entity + Star(Any(), greedy=False) + poet + Star(Any(), greedy=False)) | (poet + Star(Any(), greedy=False) + verse_entity + Star(Any(), greedy=False))), action=Question.content_search_question),
    Rule(condition_num=9, condition=((verse_entity + Star(Any(), greedy=False) + poem + Star(Any(), greedy=False)) | (poem + Star(Any(), greedy=False) + verse_entity + Star(Any(), greedy=False))), action=Question.content_search_question),
    Rule(condition_num=10, condition=(verse_entity + Star(Any(), greedy=False) + next_verse + Star(Any(), greedy=False)), action=Question.content_search_question),
    Rule(condition_num=11, condition=(verse_entity + Star(Any(), greedy=False) + prev_verse + Star(Any(), greedy=False)), action=Question.content_search_question)
]
