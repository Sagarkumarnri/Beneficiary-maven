import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from tabulate import tabulate
from datetime import datetime, timedelta

# Step 1: Load the dataset
train_file = "lead_time_data.xlsx"  # Ensure this file exists
df = pd.read_excel(train_file)

# Convert percentage column to float
df["% CRs with LTTD"] = df["% CRs with LTTD"].str.rstrip("%").astype(float) / 100.0

# Convert "Month Year" to datetime format
df["Date"] = pd.to_datetime(df["Month Year"], format="%b %y")

# Selecting features and target variable
X = df.drop(columns=["Month Year", "Lead Time To Deploy (Days)", "Date"])  # Drop non-numeric columns
y = df["Lead Time To Deploy (Days)"]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model
model = LinearRegression()
model.fit(X_scaled, y)

# Step 2: Generate future data for the next 6 months
last_date = df["Date"].max()
future_dates = [last_date + timedelta(days=30 * i) for i in range(1, 7)]  # Approximate next 6 months

# Use the mean of past data as a baseline for future predictions
future_data = pd.DataFrame({
    "Highest LTTD (Days)": [X["Highest LTTD (Days)"].mean()] * 6,
    "# CRs with LTTD": [X["# CRs with LTTD"].mean()] * 6,
    "# CRs (Closed or Review)": [X["# CRs (Closed or Review)"].mean()] * 6,
    "% CRs with LTTD": [X["% CRs with LTTD"].mean()] * 6,
    "# Pods with CRs": [X["# Pods with CRs"].mean()] * 6,
    "# Pods with LTTD": [X["# Pods with LTTD"].mean()] * 6,
    "# Assignment Groups with CRs": [X["# Assignment Groups with CRs"].mean()] * 6,
    "# Assignment Groups with LTTD": [X["# Assignment Groups with LTTD"].mean()] * 6
})

# Standardize future data
future_data_scaled = scaler.transform(future_data)

# Predict future Lead Time to Deploy
predictions = model.predict(future_data_scaled)

# Add predictions to future data
future_data["Month Year"] = [d.strftime("%b %y") for d in future_dates]
future_data["Predicted Lead Time To Deploy (Days)"] = predictions

# Save output to a new Excel file
output_file = "future_predictions.xlsx"
future_data.to_excel(output_file, index=False)
print(f"✅ Predictions saved to {output_file}")

# Step 3: Print results in tabular format
print("\n🔹 Predicted Lead Time to Deploy for Next 6 Months:\n")
print(tabulate(future_data, headers="keys", tablefmt="grid"))
