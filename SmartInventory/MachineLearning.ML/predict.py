from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# -------------------------
# Load Model
# -------------------------

model = joblib.load("inventory_model.pkl")

product_encoder = joblib.load("product_encoder.pkl")
store_encoder = joblib.load("store_encoder.pkl")
target_encoder = joblib.load("target_encoder.pkl")


@app.route("/")
def home():
    return "Smart Inventory ML API Running"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    product = product_encoder.transform([data["ProductName"]])[0]

    store = store_encoder.transform([data["StoreName"]])[0]

    df = pd.DataFrame([{
        "ProductName": product,
        "StoreName": store,
        "QuantitySold": data["QuantitySold"],
        "Revenue": data["Revenue"],
        "StockAvailable": data["StockAvailable"],
        "LeadTimeDays": data["LeadTimeDays"],
        "Promotion": data["Promotion"],
        "Month": data["Month"],
        "DayOfWeek": data["DayOfWeek"]
    }])

    prediction = model.predict(df)

    demand = target_encoder.inverse_transform(prediction)

    return jsonify({
        "PredictedDemand": demand[0]
    })


if __name__ == "__main__":
    app.run(port=5000)