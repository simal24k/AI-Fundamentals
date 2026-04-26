import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
n = 300

high_value_mask = np.random.choice([0, 1], n, p=[0.5, 0.5])

total_spending    = np.where(high_value_mask == 1,
                             np.random.randint(5000, 20000, n),
                             np.random.randint(500,  5000,  n)).astype(float)
age               = np.random.randint(18, 65, n).astype(float)
num_visits        = np.where(high_value_mask == 1,
                             np.random.randint(10, 50, n),
                             np.random.randint(1,  10, n)).astype(float)
purchase_freq     = np.where(high_value_mask == 1,
                             np.random.uniform(0.6, 1.0, n),
                             np.random.uniform(0.0, 0.5, n))

df = pd.DataFrame({
    'total_spending':  total_spending,
    'age':             age,
    'num_visits':      num_visits,
    'purchase_freq':   purchase_freq,
    'high_value':      high_value_mask
})

df.loc[np.random.choice(df.index, 8, replace=False), 'total_spending'] = np.nan
df.loc[5, 'total_spending']  = 999999
df.loc[12, 'num_visits']     = -1

print("\n[INFO] Missing values before cleaning:")
print(df.isnull().sum())

df['total_spending'] = df['total_spending'].fillna(df['total_spending'].median())

def remove_outliers(dataframe, col):
    Q1 = dataframe[col].quantile(0.25)
    Q3 = dataframe[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return dataframe[(dataframe[col] >= lower) & (dataframe[col] <= upper)]

df = remove_outliers(df, 'total_spending')
df = remove_outliers(df, 'num_visits')
df.reset_index(drop=True, inplace=True)
print(f"\n[INFO] Dataset shape after outlier removal: {df.shape}")

features = ['total_spending', 'age', 'num_visits', 'purchase_freq']
X = df[features]
y = df['high_value']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\n[INFO] Training samples : {len(X_train)}")
print(f"[INFO] Testing  samples : {len(X_test)}")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

svm = SVC(kernel='rbf', C=1, gamma='scale', random_state=42)
svm.fit(X_train_scaled, y_train)
svm_pred = svm.predict(X_test_scaled)

print("\n[RESULTS — SVM] Separating Hyperplane Classification:")
print(f"  Accuracy : {accuracy_score(y_test, svm_pred) * 100:.2f}%")
print(classification_report(y_test, svm_pred,
                             target_names=['Low-Value (0)', 'High-Value (1)']))

DT = DecisionTreeClassifier(max_depth=4, random_state=42)
DT.fit(X_train, y_train)
dt_pred = DT.predict(X_test)

print("\n[RESULTS — Decision Tree] Rule-Based Classification:")
print(f"  Training Accuracy : {DT.score(X_train, y_train) * 100:.2f}%")
print(f"  Testing  Accuracy : {accuracy_score(y_test, dt_pred) * 100:.2f}%")
print(classification_report(y_test, dt_pred,
                             target_names=['Low-Value (0)', 'High-Value (1)']))

print("[INFO] Feature Importances (Decision Tree):")
for feat, imp in zip(features, DT.feature_importances_):
    print(f"  {feat:20s}: {imp:.4f}")

print("\n[Confusion Matrix — SVM]")
cm_svm = confusion_matrix(y_test, svm_pred)
print(f"  TP={cm_svm[1][1]}  FP={cm_svm[0][1]}  FN={cm_svm[1][0]}  TN={cm_svm[0][0]}")

print("\n[Confusion Matrix — Decision Tree]")
cm_dt = confusion_matrix(y_test, dt_pred)
print(f"  TP={cm_dt[1][1]}  FP={cm_dt[0][1]}  FN={cm_dt[1][0]}  TN={cm_dt[0][0]}")
