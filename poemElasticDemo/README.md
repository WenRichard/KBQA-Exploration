
# 基于Elasticsearch的KBQA
# 上手教程

环境配置
    
    Python版本为3.6
    ElasticSearch为6.3.2
    
安装依赖包  
   - [elasticsearch-6.3.2-zip](https://www.elastic.co/cn/downloads/past-releases/elasticsearch-6-3-2)  
   - [kibana-6.3.2-windows-x86_64](https://www.elastic.co/cn/downloads/past-releases/kibana-6-3-2)  
   - Python环境中，第一步需要安装相对应的elasticsearch模块，pip install elasticsearch
   - [elasticsearch-analysis-ik分词插件](https://github.com/medcl/elasticsearch-analysis-ik)  
   - [elasticsearch-head插件](https://blog.csdn.net/u012888052/article/details/79710429)  
    直接cd到 ./elasticsearch/bin目录下，执行 elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.3.2/elasticsearch-analysis-ik-6.3.2.zip  

ElasticSearch基本操作  

    cd到目录 C:\elasticsearch-6.3.2\bin ，双击elasticsearch.bat，开启elasticsearch本地服务  
    打开网址 http://localhost:9200/ 或者 http://127.0.0.1:9200/ 查看elasticsearch基本信息
    打开网址 http://localhost:5601/ 或者 http://127.0.0.1:5601/ 查看Kibana控制界面基本信息    
    reference：  
    https://blog.csdn.net/wufaliang003/article/details/81368365
    https://blog.csdn.net/liuzemeeting/article/details/80708035
    
   
目录说明
    
    demo文件夹包含的是完成整个问答demo流程所需要的脚本。
        demo test.py
            ElasticSearch基本操作练习
        data文件夹是结巴外部词典的数据
            dynasty.txt朝代
            extendWords.txt扩展词
            poem.txt诗词名
            poet.txt诗人名
            verse.txt诗句
            Poem.csv原始数据，直接导入ElasticSearch
        elasticConnect.py
            ElasticSearch操作与数据解析
        loadData.py
            将诗词数据导入ElasticSearch
        poet_main.py
            main函数，在运行poet_main.y之前，读者需要启动ElasticSearch服务
        questionAnalysis.py
            将自然语言转为对应的查询语句
        questionMapping.py
            问题映射
        wordHandle.py
            简单语言处理

Refernec：  
[基于ElasticSearch的问答系统(KBQA)](https://blog.csdn.net/keyue123/article/details/85317774)


    
