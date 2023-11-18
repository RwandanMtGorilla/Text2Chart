import csv
from collections import Counter
import matplotlib.pyplot as plt

# 读取CSV文件并统计UFO_shape列
ufo_shape_counts = Counter()
with open('ufo-sightings-transformed.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ufo_shape_counts[row['UFO_shape']] += 1

# 按数量降序排序
sorted_shapes = sorted(ufo_shape_counts.items(), key=lambda x: x[1], reverse=True)

# 分解为两个列表：形状和计数
shapes, counts = zip(*sorted_shapes)

# 绘制条形图
plt.figure(figsize=(12, 8))
plt.bar(shapes, counts)
plt.xlabel('UFO Shape')
plt.ylabel('Number of Sightings')
plt.title('UFO Sightings by Shape')
plt.xticks(rotation=45)
plt.tight_layout()  # 调整布局以避免标签重叠
plt.show()
