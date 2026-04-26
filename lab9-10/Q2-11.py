import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage':           [150000, 120000, 250000, 80000, 100000,
                          220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency':   [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost':  [5000, 4000, 7000, 2000, 3000,
                          6500, 5500, 8000, 1500, 7500],
    'vehicle_type':      ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan',
                          'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)

print("LAB 11 - TASK 2: Vehicle Fleet Clustering")
print("\nOriginal Dataset:")
print(df.to_string(index=False))

le = LabelEncoder()
df['vehicle_type_encoded'] = le.fit_transform(df['vehicle_type'])

print("\nvehicle_type encoding:")
for cls, code in zip(le.classes_, le.transform(le.classes_)):
    print(f"  {cls} -> {code}")

numeric_features = ['vehicle_serial_no', 'mileage', 'fuel_efficiency',
                    'maintenance_cost', 'vehicle_type_encoded']

K = 3

print(f"\nRUN 1: K-Means WITHOUT Scaling  (K={K})")

X_no_scale = df[numeric_features].values
km_no = KMeans(n_clusters=K, init='k-means++', random_state=42, n_init=10)
df['Cluster_NoScale'] = km_no.fit_predict(X_no_scale)

print("\nCluster assignments (No Scaling):")
print(df[['vehicle_serial_no', 'vehicle_type', 'mileage',
          'fuel_efficiency', 'maintenance_cost',
          'Cluster_NoScale']].to_string(index=False))

print("\nCluster Centroids (original scale):")
centroid_df = pd.DataFrame(km_no.cluster_centers_, columns=numeric_features)
print(centroid_df.round(1).to_string())

print(f"\nRUN 2: K-Means WITH Scaling on numeric features (K={K})")
print("(vehicle_type is categorical - not scaled)")

cols_to_scale = ['vehicle_serial_no', 'mileage', 'fuel_efficiency', 'maintenance_cost']

scaler = StandardScaler()
scaled_numeric = scaler.fit_transform(df[cols_to_scale])
vehicle_type_col = df[['vehicle_type_encoded']].values

X_scaled = np.hstack([scaled_numeric, vehicle_type_col])

km_sc = KMeans(n_clusters=K, init='k-means++', random_state=42, n_init=10)
df['Cluster_Scaled'] = km_sc.fit_predict(X_scaled)

print("\nCluster assignments (With Scaling):")
print(df[['vehicle_serial_no', 'vehicle_type', 'mileage',
          'fuel_efficiency', 'maintenance_cost',
          'Cluster_Scaled']].to_string(index=False))

print("\nCOMPARISON")

print("\nCluster means - No Scaling:")
print(df.groupby('Cluster_NoScale')[['mileage', 'fuel_efficiency',
                                      'maintenance_cost']].mean().round(1))

print("\nCluster means - With Scaling:")
print(df.groupby('Cluster_Scaled')[['mileage', 'fuel_efficiency',
                                     'maintenance_cost']].mean().round(1))

print("""
INSIGHTS:
  Without Scaling:
    - 'mileage' (75,000-300,000) completely dominates.
    - 'fuel_efficiency' (8-24) and 'maintenance_cost' (1,500-8,000)
      are almost ignored when computing distances.
    - Clusters split purely along mileage thresholds.

  With Scaling:
    - All numeric features contribute equally.
    - Trucks (high mileage, low efficiency, high cost) form their own cluster.
    - Sedans / Hatchbacks (low mileage, high efficiency, low cost) cluster together.
    - SUVs occupy a middle cluster.
    - This is far more useful for fleet management decisions.
""")
