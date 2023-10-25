import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 生成一维数据
data = np.random.rand(100)

# 初始化KMeans模型
kmeans = KMeans(n_clusters=4)

# 对数据进行聚类
kmeans.fit(data.reshape(-1, 1))

# 获取聚类结果
labels = kmeans.labels_

# 获取聚类中心
centers = kmeans.cluster_centers_

# 绘制原始数据
plt.scatter(range(len(data)), data, c='blue', alpha=0.5, label='Original Data')

# 绘制聚类结果
plt.scatter(range(len(data)), data, c=labels, cmap='viridis', label='Clustered Data')

# 绘制聚类中心
plt.scatter(range(len(centers)), centers, c='red', marker='x', label='Cluster Centers')

plt.legend()
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('One-dimensional Clustering')
plt.show()
