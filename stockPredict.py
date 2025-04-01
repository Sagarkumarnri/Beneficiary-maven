import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from datetime import datetime, timedelta

# Load and clean stock data
df = pd.read_csv("stock_sample.csv")
df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].astype(float)

# Normalize all numeric columns
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']])

# Create sequences
seq_length = 5
X, y = [], []
for i in range(len(scaled_data) - seq_length):
    X.append(scaled_data[i:i + seq_length])
    y.append(scaled_data[i + seq_length])
X, y = np.array(X), np.array(y)

# Build LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(seq_length, 6)),
    LSTM(50),
    Dense(25),
    Dense(6)
])
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, batch_size=2, epochs=30)

# Forecast next 30 days
last_seq = scaled_data[-seq_length:]
forecasted_scaled = []

for _ in range(30):
    input_seq = last_seq.reshape((1, seq_length, 6))
    next_pred = model.predict(input_seq, verbose=0)
    forecasted_scaled.append(next_pred[0])
    last_seq = np.vstack((last_seq[1:], next_pred))

# Convert forecast back to original scale
forecasted_data = scaler.inverse_transform(np.array(forecasted_scaled))

# Generate future dates
last_date = pd.to_datetime(df["Date"].iloc[-1], format="%d-%b-%y")
future_dates = [last_date + timedelta(days=i) for i in range(1, 31)]

# Create forecast DataFrame
forecast_df = pd.DataFrame(forecasted_data, columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
forecast_df.insert(0, "Date", [d.strftime("%d-%b-%y") for d in future_dates])

# Save forecast to CSV
forecast_df.to_csv("full_stock_30_day_forecast.csv", index=False)

# Plot Close price forecast
plt.figure(figsize=(12, 6))
plt.plot(forecast_df["Date"], forecast_df["Close"], label="Forecasted Close Price")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title("30-Day Forecast: Close Price")
plt.legend()
plt.tight_layout()
plt.show()
