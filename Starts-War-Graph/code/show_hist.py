# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 21:28
# @Author  : Alan
# @Email   : xiezhengwen2013@163.com
# @File    : show_hist.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 获取数据
films_data = pd.read_csv('stat_basic.csv')
fig, ax = plt.subplots(1, 1)
print(films_data['key'])

# 设置绘图风格
sns.set_style("whitegrid")

# 最常见的是使用hls颜色空间
sns.palplot(sns.color_palette('hls',8))

# 绘制柱状图
sns.barplot(x="key", y="value", hue="title", data=films_data, ax=ax,
            palette=sns.color_palette("hls", 8))

# 设置Axes的标题
ax.set_title('Star Wars Entity Statistics')

plt.show()
