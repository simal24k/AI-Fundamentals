import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("marketing_campaign.csv", sep="\t")

features = ['Income', 'Recency', 'MntWines', 'MntMeatProducts']
df = df[features]

df = df.fillna(df.mean(numeric_only=True))

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

wcss = []

for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init='auto')
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(2, 11), wcss)
plt.title("Elbow Method")
plt.xlabel("K")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto')
labels = kmeans.fit_predict(X_scaled)

df['Cluster'] = labels

plt.scatter(df['Income'], df['MntWines'], c=labels)
plt.xlabel("Income")
plt.ylabel("Wine Spending")
plt.title("Customer Segmentation")
plt.show()

print(df.head())
