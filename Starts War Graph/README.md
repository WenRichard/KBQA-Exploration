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
