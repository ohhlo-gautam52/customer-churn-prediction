
import os
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score
import joblib

# --- 1. Ensure data directory exists ---
os.makedirs('data', exist_ok=True)

# --- 2. Load dataset ---
df = pd.read_csv('data/dataset.csv')

# --- 3. Basic EDA ---
print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data types:\n", df.dtypes)
print("Missing values:\n", df.isnull().sum())

# --- 4. Handle dates ---
df['signup_date'] = pd.to_datetime(df['signup_date'])
df['last_purchase_date'] = pd.to_datetime(df['last_purchase_date'])
current_date = datetime.now()
df['days_since_last_purchase'] = (current_date - df['last_purchase_date']).dt.days
df['days_since_signup'] = (current_date - df['signup_date']).dt.days

# --- 5. Feature engineering: Define churn ---
# Churn = 1 if days_since_last_purchase > 90 or cancellations_count > 2 or subscription_status != 'active'
df['churn'] = ((df['days_since_last_purchase'] > 90) |
               (df['cancellations_count'] > 2) |
               (df['subscription_status'] != 'active')).astype(int)
print("Churn distribution:\n", df['churn'].value_counts())

# --- 6. Select features ---
features = ['age', 'gender', 'country', 'days_since_signup', 'days_since_last_purchase',
            'cancellations_count', 'unit_price', 'quantity', 'purchase_frequency', 'category', 'Ratings']
X = df[features].copy()
y = df['churn']

# --- 7. Preprocess categorical features ---
categorical_cols = ['gender', 'country', 'category']
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    X.loc[:, col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Save all label encoders
joblib.dump(label_encoders, 'label_encoders.pkl')

# --- 8. Preprocess numeric features ---
numeric_cols = ['age', 'days_since_signup', 'days_since_last_purchase', 
                'cancellations_count', 'unit_price', 'quantity', 'purchase_frequency', 'Ratings']
scaler = StandardScaler()
X.loc[:, numeric_cols] = scaler.fit_transform(X[numeric_cols])

# Save scaler
joblib.dump(scaler, 'scaler.pkl')

# --- 9. Train-test split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 10. Train model ---
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'churn_model.pkl')

# --- 11. Evaluate model ---
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]
print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_pred_proba))

# --- 12. Predict churn probabilities for all customers ---
df['churn_probability'] = (model.predict_proba(X)[:, 1] * 100).round(2)  # as percentage

# --- 13. Save predictions ---
df[['customer_id', 'churn_probability']].to_csv('data/churn_probabilities.csv', index=False)

print("Model trained and saved. Predictions saved to data/churn_probabilities.csv")
