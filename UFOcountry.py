import csv
from collections import Counter
import matplotlib.pyplot as plt

# 读取CSV文件并统计Country列
country_counts = Counter()
with open('ufo-sightings-transformed.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        country_counts[row['Country']] += 1

# 按数量降序排序并取前30个
sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:30]

# 分解为两个列表：国家和计数
countries, counts = zip(*sorted_countries)

# 绘制条形图
plt.figure(figsize=(12, 8))  # 可以调整大小以更好地展示
plt.bar(countries, counts)
plt.xlabel('Country')
plt.ylabel('Number of UFO Sightings')
plt.title('Top 30 Countries with UFO Sightings')
plt.xticks(rotation=45)
plt.tight_layout()  # 调整布局以避免标签重叠
plt.show()
