import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
n = 500

spam_labels = np.random.choice([0, 1], n, p=[0.6, 0.4])

word_freq_free      = np.where(spam_labels == 1,
                               np.random.uniform(0.3, 1.0, n),
                               np.random.uniform(0.0, 0.2, n))
word_freq_click     = np.where(spam_labels == 1,
                               np.random.uniform(0.2, 0.8, n),
                               np.random.uniform(0.0, 0.15, n))
word_freq_money     = np.where(spam_labels == 1,
                               np.random.uniform(0.2, 0.9, n),
                               np.random.uniform(0.0, 0.1, n))
email_length        = np.where(spam_labels == 1,
                               np.random.randint(300, 2000, n),
                               np.random.randint(50, 800, n)).astype(float)
num_hyperlinks      = np.where(spam_labels == 1,
                               np.random.randint(3, 20, n),
                               np.random.randint(0, 5, n)).astype(float)
known_sender        = np.where(spam_labels == 1,
                               np.random.choice([0, 1], n, p=[0.8, 0.2]),
                               np.random.choice([0, 1], n, p=[0.2, 0.8])).astype(float)

df = pd.DataFrame({
    'word_freq_free':  word_freq_free,
    'word_freq_click': word_freq_click,
    'word_freq_money': word_freq_money,
    'email_length':    email_length,
    'num_hyperlinks':  num_hyperlinks,
    'known_sender':    known_sender,
    'is_spam':         spam_labels
})

print(f"\n[INFO] Dataset shape: {df.shape}")
print(f"[INFO] Spam emails   : {df['is_spam'].sum()}")
print(f"[INFO] Ham  emails   : {(df['is_spam'] == 0).sum()}")

features = ['word_freq_free', 'word_freq_click', 'word_freq_money',
            'email_length', 'num_hyperlinks', 'known_sender']
X = df[features]
y = df['is_spam']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

svm = SVC(kernel='rbf', C=1, gamma='scale', random_state=42)
svm.fit(X_train_scaled, y_train)

y_pred = svm.predict(X_test_scaled)

print("\n[RESULTS] Model Evaluation:")
print(f"  Accuracy : {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\n  Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Ham (0)', 'Spam (1)']))

print("  Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"            Predicted Ham  Predicted Spam")
print(f"  Actual Ham      {cm[0][0]}             {cm[0][1]}")
print(f"  Actual Spam     {cm[1][0]}             {cm[1][1]}")

print("\n[PREDICTION] Classifying new incoming emails:")

new_emails = pd.DataFrame({
    'word_freq_free':  [0.8,  0.01],
    'word_freq_click': [0.6,  0.0],
    'word_freq_money': [0.75, 0.02],
    'email_length':    [1500, 120],
    'num_hyperlinks':  [12,   1],
    'known_sender':    [0,    1]
})

new_emails_scaled = scaler.transform(new_emails)
new_preds = svm.predict(new_emails_scaled)

for i, pred in enumerate(new_preds):
    label = "SPAM" if pred == 1 else "HAM (Not Spam)"
    print(f"  Email {i + 1}: {label}")
