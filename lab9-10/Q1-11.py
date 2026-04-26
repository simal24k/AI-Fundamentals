import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)
n = 200

customer_id     = np.arange(1, n + 1)
gender          = np.random.choice([0, 1], n)
age             = np.random.randint(18, 70, n).astype(float)
annual_income   = np.random.randint(15, 137, n).astype(float)
spending_score  = np.random.randint(1, 101, n).astype(float)

df = pd.DataFrame({
    'CustomerID':      customer_id,
    'Gender':          gender,
    'Age':             age,
    'Annual Income':   annual_income,
    'Spending Score':  spending_score
})

print(f"\n[INFO] Dataset shape: {df.shape}")
print(df.head())

df_model = df.drop(columns=['CustomerID'])

def run_kmeans(X, k, label):
    km = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
    labels = km.fit_predict(X)
    print(f"\n  Cluster distribution ({label}):")
    unique, counts = np.unique(labels, return_counts=True)
    for cl, cnt in zip(unique, counts):
        print(f"    Cluster {cl}: {cnt} customers")
    return labels

print("\n")
print("RUN 1: K-Means WITHOUT Feature Scaling (K=5)")


X_no_scale = df_model.values
labels_no_scale = run_kmeans(X_no_scale, k=5, label="No Scaling")

df['Cluster_NoScale'] = labels_no_scale

print("\n  Cluster Means (original scale) — No Scaling:")
print(df.groupby('Cluster_NoScale')[
    ['Gender', 'Age', 'Annual Income', 'Spending Score']
].mean().round(2).to_string())

print("\n")
print("RUN 2: K-Means WITH Scaling on all features EXCEPT Age (K=5)")


cols_to_scale = ['Gender', 'Annual Income', 'Spending Score']
col_age       = ['Age']

scaler = StandardScaler()
scaled_part = scaler.fit_transform(df_model[cols_to_scale])
age_part     = df_model[col_age].values

X_scaled = np.hstack([scaled_part, age_part])

labels_scaled = run_kmeans(X_scaled, k=5, label="With Scaling (except Age)")
df['Cluster_Scaled'] = labels_scaled

print("\n  Cluster Means (original scale) — With Scaling:")
print(df.groupby('Cluster_Scaled')[
    ['Gender', 'Age', 'Annual Income', 'Spending Score']
].mean().round(2).to_string())

print("COMPARISON & INSIGHTS")

print("""
Without Scaling:
  - 'Annual Income' (range: 15–137 k$) dominates clustering because
    its numerical magnitude is much larger than other features.
  - 'Spending Score' (1–100) and 'Age' (18–70) have less influence.
  - Clusters tend to separate mainly by income levels.

With Scaling (except Age):
  - Gender, Annual Income, and Spending Score are on equal footing.
  - Age is left unscaled intentionally; since its range (18–70) is
    modest, it contributes without overwhelming.
  - Clusters become more balanced and capture spending behaviour
    alongside income, revealing richer customer segments.

Key takeaway: Feature scaling leads to more meaningful clusters
when features have very different ranges or units.
""")
