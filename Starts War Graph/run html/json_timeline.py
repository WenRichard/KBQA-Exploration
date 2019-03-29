# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 14:27
# @Author  : Alan
# @Email   : xiezhengwen2013@163.com
# @File    : json_timeline.py
# @Software: PyCharm

# coding:utf8
import time
import json

# 定义六类实体
films = []
characters = []
planets = []
starships = []
vehicles = []
species = []

fr = open('../films.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    films.append(tmp)
fr.close()

fr = open('../film_characters.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    characters.append(tmp)
fr.close()

fr = open('../film_planets.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    planets.append(tmp)
fr.close()

fr = open('../film_starships.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    starships.append(tmp)
fr.close()

fr = open('../film_vehicles.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    vehicles.append(tmp)
fr.close()

fr = open('../film_species.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    species.append(tmp)
fr.close()

# 输出各类实体数量
# 7 87 21 37 39 37
print(len(films), len(characters), len(planets), len(starships), len(vehicles), len(species))

data = []

# 遍历每个人物在电影里是否出现过
for item in characters:
    tmp = []
    for film in films:
        flag = False  # 标志变量 初始值未出现过
        for f in film['characters']:
            # 如果人的url在电影f里出现过跳出循环
            if item['url'] == f:
                flag = True
                break
        if flag:  # 如果人没有则添加至变量tmp中
            tmp.append(1)
        else:
            tmp.append(0)  # 没出现在这部电影里
    # 数据存储至data变量中
    # 名字 类型 组(着色) tmp对应是否出现向量
    data.append({'name': item['name'], 'type': 'character', 'group': 0, 'vector': tmp})

# 星球
for item in planets:
    tmp = []
    for film in films:
        flag = False
        for f in film['planets']:
            if item['url'] == f:
                flag = True
                break
        if flag:
            tmp.append(1)
        else:
            tmp.append(0)
    data.append({'name': item['name'], 'type': 'planet', 'group': 1, 'vector': tmp})

for item in starships:
    tmp = []
    for film in films:
        flag = False
        for f in film['starships']:
            if item['url'] == f:
                flag = True
                break
        if flag:
            tmp.append(1)
        else:
            tmp.append(0)
    data.append({'name': item['name'], 'type': 'starship', 'group': 2, 'vector': tmp})

for item in vehicles:
    tmp = []
    for film in films:
        flag = False
        for f in film['vehicles']:
            if item['url'] == f:
                flag = True
                break
        if flag:
            tmp.append(1)
        else:
            tmp.append(0)
    data.append({'name': item['name'], 'type': 'vehicle', 'group': 3, 'vector': tmp})

for item in species:
    tmp = []
    for film in films:
        flag = False
        for f in film['species']:
            if item['url'] == f:
                flag = True
                break
        if flag:
            tmp.append(1)
        else:
            tmp.append(0)
    data.append({'name': item['name'], 'type': 'species', 'group': 4, 'vector': tmp})

# 将电影存储
# 将电影和数据装载至Json文件中 7部电影 221个节点
films = [[films[x]['title'], films[x]['release_date']] for x in range(0, len(films))]
result = {'films': films, 'data': data}

fw = open('all_timeline.json', 'w')
fw.write(json.dumps(result))
fw.close()
