# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 21:55
# @Author  : Alan
# @Email   : xiezhengwen2013@163.com
# @File    : show_height_mass.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 读取数据
df = pd.read_csv('stat_character.csv')
fig, ax = plt.subplots(1, 1)

# name height mass gender homeworld
# 散点图
sns.jointplot(x="height", y="mass", data=df, color="b", s=50, kind='scatter',
              space = 0.1, size = 8, ratio = 5)
plt.show()

# 回归图
sns.jointplot(x="height", y="mass", data=df, color="b", kind='reg')

plt.show()

# 六角形
sns.jointplot(x="height", y="mass", data=df, color="b", kind='hex')

plt.show()

# KDE 图
sns.jointplot(x="height", y="mass", data=df, kind="kde", space=0, color="#6AB27B")

plt.show()

# 散点图+KDE 图
g = (sns.jointplot(x="height", y="mass", data=df, color="k")
      .plot_joint(sns.kdeplot, zorder=0, n_levels=6))

plt.show()

sns.pairplot(df)

plt.show()



