import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)
n = 120

student_id = [f"STU{str(i).zfill(3)}" for i in range(1, n + 1)]

group = np.random.choice([0, 1, 2], n, p=[0.3, 0.4, 0.3])

gpa = np.where(group == 0, np.random.uniform(1.5, 2.4, n),
      np.where(group == 1, np.random.uniform(2.4, 3.3, n),
                           np.random.uniform(3.3, 4.0, n))).round(2)

study_hours = np.where(group == 0, np.random.uniform(2,  8,  n),
              np.where(group == 1, np.random.uniform(8,  16, n),
                                   np.random.uniform(16, 25, n))).round(1)

attendance_rate = np.where(group == 0, np.random.uniform(40, 65, n),
                  np.where(group == 1, np.random.uniform(65, 80, n),
                                       np.random.uniform(80, 100, n))).round(1)

df = pd.DataFrame({
    'student_id':      student_id,
    'GPA':             gpa,
    'study_hours':     study_hours,
    'attendance_rate': attendance_rate
})

print("LAB 11 - TASK 3: Student Academic Clustering")
print(f"\nDataset shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head().to_string(index=False))

print("\nBasic statistics:")
print(df[['GPA', 'study_hours', 'attendance_rate']].describe().round(2))

features = ['GPA', 'study_hours', 'attendance_rate']
X = df[features].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nFeatures selected:", features)
print("StandardScaler applied.")

print("\nRunning Elbow Method (K = 2 to 6)...")

wcss_list = []
k_range = range(2, 7)

for k in k_range:
    km = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
    km.fit(X_scaled)
    wcss_list.append(km.inertia_)
    print(f"  K={k}  WCSS={km.inertia_:.4f}")

plt.figure(figsize=(7, 4))
plt.plot(list(k_range), wcss_list, marker='o', color='steelblue', linewidth=2)
plt.title('Elbow Method - Optimal K for Student Clusters', fontsize=13)
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.xticks(list(k_range))
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('student_elbow.png', dpi=150)
plt.show()
print("\nElbow plot saved as 'student_elbow.png'")

OPTIMAL_K = 3

print(f"\nOptimal K selected: {OPTIMAL_K}")

km_final = KMeans(n_clusters=OPTIMAL_K, init='k-means++', random_state=42, n_init=10)
df['Cluster'] = km_final.fit_predict(X_scaled)

cluster_means = df.groupby('Cluster')['GPA'].mean().sort_values()
label_map = {}
labels_text = ['Struggling', 'Average', 'High-Achiever']
for i, (cluster_id, _) in enumerate(cluster_means.items()):
    label_map[cluster_id] = labels_text[i]

df['Cluster_Label'] = df['Cluster'].map(label_map)

print("\nFinal Dataset with Cluster Assignments:")
print(df[['student_id', 'GPA', 'study_hours',
          'attendance_rate', 'Cluster', 'Cluster_Label']].to_string(index=False))

print("\nCluster Summary:")
summary = df.groupby('Cluster_Label')[['GPA', 'study_hours', 'attendance_rate']].mean().round(2)
summary['Count'] = df.groupby('Cluster_Label')['student_id'].count()
print(summary.to_string())

colors = ['#e74c3c', '#3498db', '#2ecc71']
cluster_labels_sorted = ['Struggling', 'Average', 'High-Achiever']

plt.figure(figsize=(9, 6))

for i, (cl, color) in enumerate(zip(cluster_labels_sorted, colors)):
    subset = df[df['Cluster_Label'] == cl]
    plt.scatter(subset['study_hours'], subset['GPA'],
                c=color, label=cl, s=80, edgecolors='white',
                linewidths=0.5, alpha=0.85)

centroids_original = scaler.inverse_transform(km_final.cluster_centers_)
centroid_df = pd.DataFrame(centroids_original, columns=features)
centroid_df['Cluster'] = range(OPTIMAL_K)
centroid_df['Cluster_Label'] = centroid_df['Cluster'].map(label_map)
centroid_df_sorted = centroid_df.sort_values('GPA')

for i, (_, row) in enumerate(centroid_df_sorted.iterrows()):
    plt.scatter(row['study_hours'], row['GPA'],
                c='black', marker='X', s=200, zorder=5,
                label='Centroid' if i == 0 else '')

plt.title('Student Academic Clusters (K-Means, K=3)\nX-axis: Study Hours/week   |   Y-axis: GPA',
          fontsize=13, fontweight='bold')
plt.xlabel('Study Hours per Week', fontsize=12)
plt.ylabel('GPA', fontsize=12)
plt.legend(title='Cluster', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('student_clusters_scatter.png', dpi=150)
plt.show()
print("\nScatter plot saved as 'student_clusters_scatter.png'")
