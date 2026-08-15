import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# --------------------------
# Load Dataset
# --------------------------

df = pd.read_csv("sales_data.csv")

print("Dataset Loaded Successfully")
print(df.head())

# --------------------------
# Encode Categorical Columns
# --------------------------

product_encoder = LabelEncoder()
store_encoder = LabelEncoder()
target_encoder = LabelEncoder()

df["ProductName"] = product_encoder.fit_transform(df["ProductName"])
df["StoreName"] = store_encoder.fit_transform(df["StoreName"])
df["DemandLevel"] = target_encoder.fit_transform(df["DemandLevel"])

# --------------------------
# Features and Target
# --------------------------

X = df[
    [
        "ProductName",
        "StoreName",
        "QuantitySold",
        "Revenue",
        "StockAvailable",
        "LeadTimeDays",
        "Promotion",
        "Month",
        "DayOfWeek",
    ]
]

y = df["DemandLevel"]

# --------------------------
# Train Test Split
# --------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------
# Train Model
# --------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# --------------------------
# Evaluate
# --------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)

print("\nClassification Report\n")
print(classification_report(
    y_test,
    predictions,
    target_names=target_encoder.classes_
))

# --------------------------
# Save Model
# --------------------------

joblib.dump(model, "inventory_model.pkl")

joblib.dump(product_encoder, "product_encoder.pkl")
joblib.dump(store_encoder, "store_encoder.pkl")
joblib.dump(target_encoder, "target_encoder.pkl")

print("\nModel Saved Successfully!")