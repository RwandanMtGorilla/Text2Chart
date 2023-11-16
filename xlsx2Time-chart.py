import pandas as pd
import jieba
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
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

# 初始化字典来存储每个词在每个年份的出现次数
yearly_word_counts = defaultdict(lambda: Counter())

# 统计每个年份每个词的出现次数
for _, row in df.iterrows():
    year = row['年份']
    words = row['发明名称分词']
    yearly_word_counts[year].update(words)

# 汇总所有年份的数据
total_counts = Counter()
for year in yearly_word_counts:
    total_counts.update(yearly_word_counts[year])

# 选取频率最高的前15个词
top_n = 15
top_words = [word for word, count in total_counts.most_common(top_n)]

# 准备数据以绘制折线图
years = range(2014, 2024)
lines_data = {word: [yearly_word_counts[year][word] for year in years] for word in top_words}

# 绘制折线图
plt.figure(figsize=(15, 8))
for word, counts in lines_data.items():
    plt.plot(years, counts, marker='o', label=word)

plt.xlabel('Year')
plt.ylabel('Frequency')
plt.title('Frequency of Top 15 Words Over Time')
plt.xticks(np.arange(2014, 2024, 1))
plt.legend()
plt.show()
