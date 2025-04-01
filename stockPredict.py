import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load stock data
df = pd.read_csv("stock_sample.csv")  # Replace with your CSV file
df = df[['Close']]  # Use only the "Close" price

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
df_scaled = scaler.fit_transform(df)

# Create sequences for LSTM
def create_sequences(data, seq_length):
    sequences = []
    labels = []
    for i in range(len(data) - seq_length):
        sequences.append(data[i:i + seq_length])
        labels.append(data[i + seq_length])
    return np.array(sequences), np.array(labels)

seq_length = 50  # Adjust sequence length as needed
X, y = create_sequences(df_scaled, seq_length)

# Split into training and testing sets
train_size = int(len(X) * 0.8)
X_train, y_train = X[:train_size], y[:train_size]
X_test, y_test = X[train_size:], y[train_size:]

# Build LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(seq_length, 1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, batch_size=16, epochs=20, validation_data=(X_test, y_test))

# Make predictions
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)  # Convert back to original scale

# Save forecasted data
forecast_df = pd.DataFrame(predictions, columns=["Predicted_Close"])
forecast_df.to_csv("forecasted_stock_data.csv", index=False)

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(df.index[train_size + seq_length:], df["Close"].iloc[train_size + seq_length:], label="Actual Prices")
plt.plot(df.index[train_size + seq_length:], predictions, label="Predicted Prices", linestyle="dashed")
plt.legend()
plt.show()
