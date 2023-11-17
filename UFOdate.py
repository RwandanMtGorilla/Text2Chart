import csv
from collections import Counter
import matplotlib.pyplot as plt

# 读取csv文件
with open('ufo-sightings-transformed.csv', 'r') as f:
    reader = csv.DictReader(f)
    # 修改为先按年份，再按月份排序
    year_month = sorted([(int(row['Year']), int(row['Month'])) for row in reader])

# 统计每一个年月组合出现的次数
counter = Counter(year_month)

# 将年月组合和出现次数分别存入两个列表
dates = [f'{year}/{month:02d}' for year, month in counter.keys()]
counts = list(counter.values())

# 画图
plt.figure(figsize=(10, 6))
plt.plot(dates, counts)
# 修改为每隔20个日期显示一个
plt.xticks(range(0, len(dates), 15), dates[::15], rotation=90)
plt.xlabel('Date (Year/Month)')
plt.ylabel('Number of Sightings')
plt.title('UFO Sightings by Year and Month')
plt.tight_layout()
plt.show()