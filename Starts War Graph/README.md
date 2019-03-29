---
title: 星球大战知识图谱  
date: 2019.3
categories:
- 知识图谱初探
- 简单demo
tags:
- 练习
Team: 一梦南柯
---
* [目录](#0)
   * [数据爬取](#1)
   * [数据分析](#2)
   * [实体抽取，关系抽取](#3)
   * [可视化展示](#4)
   * [Reference](#5)
   
<h1 id="1">一、数据爬取</h1>    

数据爬取：[SWAPI 网站](https://swapi.co/documentation)  
数据格式简览：  
![baidu]( https://github.com/WenRichard/Intelligent-Furniture-FAQ/raw/master/Image/百度AnyQ.png "百度AnyQ Framework") 
* #### get_files.py  
爬虫获取基本电影的数据，循环遍历 https://swapi.co/api/films/7 七部电影的信息  
* #### get_details.py  
遍历每部电影films的实体并通过解析链接获取其他实体  
* #### get_jsonfilms.py  
获取各部电影的实体数量  
* #### show_hist.py  
柱状图绘制
* #### get_jsondetails.py  
获取 film_characters.csv 人物文件中，各人物身体的身高、体重、性别、家乡

<h1 id="2">一、数据分析</h1> 

* #### show_scatter.py  
matplotlib绘制散点图  
* #### show_height_mass.py  
seaborn散点图，回归图，六角形，KDE图，散点图+KDE 图  
分析图部分展示：  
![baidu]( https://github.com/WenRichard/Intelligent-Furniture-FAQ/raw/master/Image/百度AnyQ.png "百度AnyQ Framework") 

<h1 id="3">一、实体抽取，关系抽取</h1> 

**可视化展示通报包括两种方法：**  
1.写入数据库，后台获取数据库中数据并展示，推荐Neo4j图数据库  
2.将数据写入Json格式文件，然后前端用Ajax请求数据展示    
本项目采用第二种  
### 3.1 实体抽取，关系抽取    
#### get_alldata_json.py  
1.	第一步读取数据。定义六类实体字典，循环获取各实体对应的超链接  
2.	第二步获取节点(Nodes)和边(Links)并存储至本地JSON文件中。其中节点为六大类，关系为它们之间互为关联，并定义节点属性（名称、类别、大小等）和关系属性（起始点、结束点、大小）  
#### 探究Starts War中的节点和边的多种关系  
**nodes实体属性：**  
包括 **id、class、group、size**  
如：{'id': value['title'], 'class': 'film', 'group': 0, 'size': 20}  
- Id：实体名称
- Class：实体类型，取值：film，character，planet，starship，vehicle，species
- Group：取值0-5，6个组
- Size：20，5，16，8，8，14，

**links属性：**  
**边的种类如下：**  
1.films：如果电影中的人物在人物集中，则建立film到character的边  
2.character：建立character到film的边，同理建立character到homeworld的边，character到species的边， character到starships的边，character到vehicles的边等  
3.planets：建立planet到filem的边，planet到character的边  
4.starships：建立starships到film的边，建立starships到character的边  
5.vehicles：建立vehicles到film的边，建立vehicles到character的边  
6.species：建立species到planets的边，建立species到film的边  
如：{'source': value['title'], 'target': characters[item]['name'], 'value': 3}  
- Source：start实体名称
- Target：end实体名称
- Value：边的权重设置为3




