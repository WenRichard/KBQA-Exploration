
# 基于Elasticsearch的KBQA
# 上手教程

环境配置
    
    Python版本为3.7
    ElasticSearch为6.4.2

目录说明
    
    demo文件夹包含的是完成整个问答demo流程所需要的脚本。
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
