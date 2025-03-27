import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_excel("lead_time_data.xlsx")

# Convert percentage column to float
df["% CRs with LTTD"] = df["% CRs with LTTD"].str.rstrip("%").astype(float) / 100.0

# Selecting features and target variable
X = df.drop(columns=["Month Year", "Lead Time To Deploy (Days)"])  # Drop non-numeric column
y = df["Lead Time To Deploy (Days)"]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Fit on full dataset

# Train the model on full dataset
model = LinearRegression()
model.fit(X_scaled, y)

# Manually input values for prediction
manual_input = pd.DataFrame([{
    "Highest LTTD (Days)": 500,  # Example value
    "# CRs with LTTD": 20,
    "# CRs (Closed or Review)": 40,
    "% CRs with LTTD": 0.60,  # Example: 60% converted to decimal
    "# Pods with CRs": 15,
    "# Pods with LTTD": 10,
    "# Assignment Groups with CRs": 12,
    "# Assignment Groups with LTTD": 8
}])

# Standardize manual input using the same scaler
manual_input_scaled = scaler.transform(manual_input)

# Predict lead time to deploy
prediction = model.predict(manual_input_scaled)

# Output prediction
print("Predicted Lead Time to Deploy (Days):", prediction[0])
