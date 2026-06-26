from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# ==========================
# Load Model & Columns
# ==========================

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("quikr_car.csv")

companies = sorted(df["company"].dropna().unique())
fuel_types = sorted(df["fuel_type"].dropna().unique())

# Company -> Models Dictionary
company_models = {}

for company in companies:
    company_models[company] = sorted(
        df[df["company"] == company]["name"].dropna().unique().tolist()
    )

# ==========================
# Home Page
# ==========================

@app.route("/")
def home():

    return render_template(
        "index.html",
        companies=companies,
        fuel_types=fuel_types,
        company_models=company_models,
        prediction=None
    )

# ==========================
# Prediction
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    company = request.form["company"]
    car_model = request.form["car_model"]
    fuel_type = request.form["fuel_type"]

    year = int(request.form["year"])
    kms_driven = int(request.form["kms_driven"])

    # Create Input DataFrame
    input_df = pd.DataFrame(0, index=[0], columns=columns)

    # Numerical Features
    if "year" in input_df.columns:
        input_df.loc[0, "year"] = year

    if "kms_driven" in input_df.columns:
        input_df.loc[0, "kms_driven"] = kms_driven

    # One-Hot Encoded Features

    company_col = f"company_{company}"
    model_col = f"name_{car_model}"
    fuel_col = f"fuel_type_{fuel_type}"

    if company_col in input_df.columns:
        input_df.loc[0, company_col] = 1

    if model_col in input_df.columns:
        input_df.loc[0, model_col] = 1

    if fuel_col in input_df.columns:
        input_df.loc[0, fuel_col] = 1

    # Predict
    predicted_price = model.predict(input_df)[0]

    predicted_price = max(0, predicted_price)

    return render_template(
        "index.html",
        companies=companies,
        fuel_types=fuel_types,
        company_models=company_models,
        prediction=f"{predicted_price:,.0f}"
    )

# ==========================
# Run Application
# ==========================

if __name__ == "__main__":
    app.run(debug=True)