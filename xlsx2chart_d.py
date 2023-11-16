import pandas as pd
import jieba
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from matplotlib.font_manager import FontProperties

# 设置matplotlib的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统使用SimHei
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负

# 读取表格文件
df = pd.read_excel('input.xlsx')  # 替换成你的文件路径

# 从“申请日”列提取年份
df['年份'] = pd.to_datetime(df['申请日']).dt.year

# 对“发明名称”进行分词
df['发明名称分词'] = df['摘要'].apply(lambda x: jieba.lcut(x))

# 读取停用词
with open('stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set([line.strip() for line in file])

# 去除停用词
df['发明名称分词'] = df['发明名称分词'].apply(lambda x: [word for word in x if word not in stopwords])

# 分割数据集为2020年前和2020年后
df_pre_2020 = df[df['年份'] < 2020]
df_post_2020 = df[df['年份'] >= 2020]

# 统计2020年前后的词频
word_counts_pre_2020 = Counter(word for words in df_pre_2020['发明名称分词'] for word in words)
word_counts_post_2020 = Counter(word for words in df_post_2020['发明名称分词'] for word in words)

# 选择前N个最常见的词
top_n = 15
top_words_pre_2020, top_counts_pre_2020 = zip(*word_counts_pre_2020.most_common(top_n))
top_words_post_2020, top_counts_post_2020 = zip(*word_counts_post_2020.most_common(top_n))

# 绘制柱状图（2020年前）
plt.figure(figsize=(12, 6))
plt.bar(top_words_pre_2020, top_counts_pre_2020)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top Words in Patent Names Before 2020')
plt.xticks(rotation=45)
plt.show()

# 绘制柱状图（2020年后）
plt.figure(figsize=(12, 6))
plt.bar(top_words_post_2020, top_counts_post_2020)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top Words in Patent Names After 2020')
plt.xticks(rotation=45)
plt.show()
