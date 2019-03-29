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

### 数据爬取：[SWAPI 网站](https://swapi.co/documentation)  
### 数据格式简览：  
![baidu]( https://github.com/WenRichard/Intelligent-Furniture-FAQ/raw/master/Image/百度AnyQ.png "百度AnyQ Framework") 
* ### get_files.py  
爬虫获取基本电影的数据，循环遍历 https://swapi.co/api/films/7 七部电影的信息  
* ### get_details.py  
遍历每部电影films的实体并通过解析链接获取其他实体  
* ### get_jsonfilms.py  
获取各部电影的实体数量  
* ### show_hist.py  
柱状图绘制
* ### get_jsondetails.py  
获取 film_characters.csv 人物文件中，各人物身体的身高、体重、性别、家乡

<h1 id="2">二、数据分析</h1> 

* ### show_scatter.py  
matplotlib绘制散点图  
* ### show_height_mass.py  
seaborn散点图，回归图，六角形，KDE图，散点图+KDE 图  
### 分析图部分展示：  
![baidu]( https://github.com/WenRichard/Intelligent-Furniture-FAQ/raw/master/Image/百度AnyQ.png "百度AnyQ Framework") 

<h1 id="3">三、实体抽取，关系抽取</h1> 

### 可视化展示通报包括两种方法：   
1.写入数据库，后台获取数据库中数据并展示，推荐Neo4j图数据库  
2.将数据写入Json格式文件，然后前端用Ajax请求数据展示    
本项目采用第二种  
### 3.1 实体抽取，关系抽取    
### 一. get_alldata_json.py  
  1.	第一步读取数据。定义六类实体字典，循环获取各实体对应的超链接  
  2.	第二步获取节点(Nodes)和边(Links)并存储至本地JSON文件中。其中节点为六大类，关系为它们之间互为关联，并定义节点属性（名称、类别、大小等）和关系属性（起始点、结束点、大小）  
### 二. 探究Starts War中的节点和边的多种关系  
**nodes实体属性：**  
包括 **id、class、group、size**  
如：{**'id'**: value['title'], **'class'**: 'film', **'group'**: 0, **'size'**: 20}  
- Id：实体名称
- Class：实体类型，取值：film，character，planet，starship，vehicle，species
- Group：取值0-5，6个组
- Size：20，5，16，8，8，14，

**links属性：**  
**边的种类如下：**  
1. **films：** film --> character 
2. **character：** character --> film, character --> homeworld， character --> species， character --> starships， character -->  vehicles  
3. **planets：** planet --> filem， planet --> character  
4. **starships：** starships --> film， starships --> character    
5. **vehicles：** vehicles --> film， vehicles --> character   
6. **species：** species --> planets， species --> film    

如：{**'source'**: value['title'], **'target'**: characters[item]['name'], **'value'**: 3}  
- Source：start实体名称
- Target：end实体名称
- Value：边的权重设置为3

<h1 id="1">四、可视化展示</h1>  

### Pipeline 如下：
### 1. 页面布局
**要点：掌握D3获取JSON数据展示的过程，然后将其加载至更好的或开源的前端中**
1.  加载JQuery样式  
2.  增加D3（Data-Driven Documents）库，它是非常流行的可视化库  
### 2. 绘制图例
通过JS获取SVG1布局，并加载六种颜色，对应六个图例。再设置 indicator 图例布局，动态加载颜色  
### 3. D3获取JSON数据
调用D3获取JSON文件数据，利用d3.forceSimulation()定义关系图 包括设置边link、排斥电荷charge、关系图中心点。
### 4. D3设置节点和关系，绘制关系图谱  
1. 定义d3.json请求python处理好的节点及边  
2. 通过D3映射数据至HTML中  
### 5. HTML和CSS添加两个span节点，提供2个按钮  
### 6. D3实现两种模式下的图形切换  
### 7. D3鼠标事件显示相关联的节点  
### 8. D3鼠标事件显示相关联的边  
### 9. D3实现鼠标移开图形还原  
### 10. D3实现文字部分鼠标事件  
### 11. D3获取并显示属性-属性值  
### 12. HTML增加搜索框  
### 13. JS增加搜索响应事件  
### 14. 优化代码-显示相关联节点及边  
**我们更期待的结果是反馈搜索节点及其相关联的边及节点**  
方法：增加一个循环，判断所有边的起点（Source）或终点（Target）与该搜索节点相邻，则显示，否则设置其class属性为’inactive’，即隐藏节点

