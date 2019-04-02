#!/usr/bin/python                                                                                                                                                                                                                
# coding=utf-8

# File Name: poet_main.py
# Author   : john
# company  : foxconn
# Mail     : john.y.ke@mail.foxconn.com 
# Created Time: 2018/12/25 10:37
# Describe : 主函数

import questionAnalysis
import elasticConnect

if __name__ == '__main__':
    es = elasticConnect.ElasticConnect()
    q2s = questionAnalysis.QuestionMatch(['./data/poem.txt', './data/poet.txt', './data/dynasty.txt',
                                          './data/verse.txt', './data/extendWords.txt'])

    while True:
        question = input("请输入问题(q退出): ")
        if question == 'q':
            break

        num, values = q2s.get_resukt(question)
        if values is not None:
            query = es.query_search(values)
            results = es.get_result(num, query)
            if len(results):
                if num < 10:
                    print("、".join(results))
                else:
                    words = results[0].split('，')
                    poemLen = len(words)
                    count = 0
                    for word in words:
                        if word in question:
                            if ("下一句" in question) | ("下句" in question):
                                if count < (poemLen-2):
                                    print(words[count + 1])
                                else:
                                    print("亲，已经到最后一句了喔")
                                break
                            if ("上一句" in question) | ("上句" in question):
                                if count == 0:
                                    print("亲，这是第一句，没了上句啦")
                                else:
                                    print(words[count - 1])
                                break
                        count = count + 1
            else:
                print("没有找你要的答案，我会继续努力学习的喔")
        else:
            print('我没有理解你说的是啥子')