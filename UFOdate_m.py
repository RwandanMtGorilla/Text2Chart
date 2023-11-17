import csv
from collections import Counter
import matplotlib.pyplot as plt

# 读取csv文件
with open('ufo-sightings-transformed.csv', 'r') as file:
    reader = csv.DictReader(file)
    months = [row['Month'] for row in reader]

# 统计月份的频率
counter = Counter(months)

# 为了使x轴的月份按照顺序显示，我们需要对counter的keys进行排序
months = sorted(counter.keys(), key=int)  # 将月份从字符串转换为整数进行排序
counts = [counter[month] for month in months]

# 绘制统计图
plt.figure(figsize=(10,6))
plt.bar(months, counts)
plt.xlabel('Month')
plt.ylabel('Number of UFO sightings')
plt.title('Number of UFO sightings by month')
plt.show()