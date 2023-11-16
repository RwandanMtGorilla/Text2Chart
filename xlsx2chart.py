import pandas as pd
import jieba
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.font_manager import FontProperties

# 设置matplotlib的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统使用SimHei
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负
# 读取表格文件
df = pd.read_excel('input.xlsx')  # 替换成你的文件路径

# 对“发明名称”进行分词
df['发明名称分词'] = df['发明名称'].apply(lambda x: jieba.lcut(x))

# 读取停用词
with open('stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set([line.strip() for line in file])

# 去除停用词
df['发明名称分词'] = df['发明名称分词'].apply(lambda x: [word for word in x if word not in stopwords])

# 统计词频
word_counts = Counter(word for words in df['发明名称分词'] for word in words)

# 对词频进行排序
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# 取前N个词进行展示
top_n = 30
top_words, top_counts = zip(*sorted_word_counts[:top_n])

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(top_words, top_counts)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top Words in Patent Names')
plt.xticks(rotation=45)
plt.show()
