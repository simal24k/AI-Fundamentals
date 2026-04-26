import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

np.random.seed(42)
n = 200

neighborhoods = ['Downtown', 'Suburb', 'Rural', 'Uptown']
neighborhood_col = np.random.choice(neighborhoods, n)

sqft        = np.random.randint(500, 5000, n)
bedrooms    = np.random.randint(1, 6, n)
bathrooms   = np.random.randint(1, 4, n)
age         = np.random.randint(1, 50, n)

base_price = (sqft * 150 + bedrooms * 10000 + bathrooms * 8000 - age * 500)
noise      = np.random.randint(-20000, 20000, n)

neighborhood_bonus = {'Downtown': 50000, 'Suburb': 20000,
                      'Rural': 0,       'Uptown': 70000}
nb_bonus = np.array([neighborhood_bonus[nb] for nb in neighborhood_col])

price = base_price + nb_bonus + noise

df = pd.DataFrame({
    'sqft':         sqft,
    'bedrooms':     bedrooms,
    'bathrooms':    bathrooms,
    'age':          age,
    'neighborhood': neighborhood_col,
    'price':        price
})

df.loc[np.random.choice(df.index, 10, replace=False), 'sqft']    = np.nan
df.loc[np.random.choice(df.index, 5,  replace=False), 'bedrooms'] = np.nan

print("\n[INFO] Missing values before cleaning:")
print(df.isnull().sum())

df['sqft']     = df['sqft'].fillna(df['sqft'].median())
df['bedrooms'] = df['bedrooms'].fillna(df['bedrooms'].median())

print("\n[INFO] Missing values after cleaning:")
print(df.isnull().sum())

le = LabelEncoder()
df['neighborhood_encoded'] = le.fit_transform(df['neighborhood'])

print("\n[INFO] Neighborhood encoding map:")
for cls, code in zip(le.classes_, le.transform(le.classes_)):
    print(f"  {cls} -> {code}")

features = ['sqft', 'bedrooms', 'bathrooms', 'age', 'neighborhood_encoded']
X = df[features]
y = df['price']

print(f"\n[INFO] Features used: {features}")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\n[INFO] Training samples : {len(X_train)}")
print(f"[INFO] Testing  samples : {len(X_test)}")

LR = LinearRegression()
LR.fit(X_train, y_train)

y_pred = LR.predict(X_test)

mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("\n[RESULTS] Model Evaluation:")
print(f"  RMSE : {rmse:,.2f}")
print(f"  R²   : {r2:.4f}  ({r2 * 100:.2f}%)")

print("\n[INFO] Model Coefficients:")
for feat, coef in zip(features, LR.coef_):
    print(f"  {feat:25s}: {coef:,.2f}")
print(f"  {'Intercept':25s}: {LR.intercept_:,.2f}")

new_house = pd.DataFrame([[2000, 3, 2, 10,
                            le.transform(['Uptown'])[0]]],
                          columns=features)

predicted_price = LR.predict(new_house)[0]
print("\n[PREDICTION] New house features:")
print(f"  sqft=2000, bedrooms=3, bathrooms=2, age=10, neighborhood=Uptown")
print(f"  Predicted Price: PKR / $ {predicted_price:,.2f}")
