# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv('https://raw.githubusercontent.com/Ayansinha12/Vityarthi-AIML-project/main/stock_data_2000_2025.csv')

# Convert Date column
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values('Date')

# Convert to ordinal
data['Date_ordinal'] = data['Date'].map(pd.Timestamp.toordinal)

# Features and target
X = data[['Date_ordinal']]
y = data['Close']

poly = PolynomialFeatures(degree=4)   # change 3 or 4 if needed
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

input_date = pd.to_datetime(input("Enter date (YYYY-MM-DD): "))
days_range = int(input("Enter number of days to display around date: "))

#Filter range
start_date = input_date - pd.Timedelta(days=days_range)
end_date = input_date + pd.Timedelta(days=days_range)

filtered_data = data[(data['Date'] >= start_date) &
                     (data['Date'] <= end_date)].copy()
X_range_poly = poly.transform(filtered_data[['Date_ordinal']])
filtered_data['Predicted'] = model.predict(X_range_poly)

#Plot
plt.figure(figsize=(12,6))

# Actual line
plt.plot(filtered_data['Date'], filtered_data['Close'],
         marker='o', label='Actual Price')
plt.plot(filtered_data['Date'], filtered_data['Predicted'],
         linestyle='dashed', marker='x', label='Predicted Price')

#Highlight selected date
input_ordinal = input_date.toordinal()
predicted_price = model.predict(poly.transform([[input_ordinal]]))[0]

if input_date in list(data['Date']):
    actual_price = data[data['Date'] == input_date]['Close'].values[0]
    plt.scatter(input_date, actual_price, s=120, label='Actual (Selected)')
    plt.text(input_date, actual_price, f"{actual_price:.2f}", ha='right')

plt.scatter(input_date, predicted_price, s=120, marker='x', label='Predicted (Selected)')
plt.text(input_date, predicted_price, f"{predicted_price:.2f}", ha='left')

# Labels
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Stock Price with Zig-Zag Prediction (Polynomial Regression)')
plt.legend()
plt.grid()

plt.show()
