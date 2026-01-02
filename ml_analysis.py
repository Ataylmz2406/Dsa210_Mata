import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, classification_report, confusion_matrix


try:
    weather = pd.read_csv('kadikoy_weather_2024_2025.csv', parse_dates=['time'], index_col='time')
    aq = pd.read_csv('kadikoy_air_quality_2024_2025.csv', parse_dates=['time'], index_col='time')
except FileNotFoundError:
    print("CSV files not found.")
    exit()

# Handle timezones
if aq.index.tz is not None: aq.index = aq.index.tz_localize(None)
if weather.index.tz is not None: weather.index = weather.index.tz_localize(None)

# Merge datasets and Drop missing values
df = pd.merge(weather, aq, left_index=True, right_index=True, how='inner')
df = df.dropna()
df['hour'] = df.index.hour
df['day_of_week'] = df.index.dayofweek
df['month'] = df.index.month
df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)

# Define Features
features = ['temperature', 'humidity', 'precipitation', 'wind_speed', 'wind_direction', 'hour', 'month', 'is_weekend']
target = 'pm10'
X = df[features]
y = df[target]

print(f"{X.shape[0]} observations")

# Split into Train and Test 80/20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# random forest
print("\nRandom Forest")
regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(X_train, y_train)

# Predictions
y_pred_reg = regressor.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred_reg)
r2 = r2_score(y_test, y_pred_reg)

print(f"Model Performance:")
print(f"Mean Absolute Error: {mae:.2f} µg/m³ (On average, predictions are off by this amount)")
print(f"R2 Score: {r2:.2f} (Explains {r2*100:.1f}% of the variance)")

# Plotting Results
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred_reg, alpha=0.5)
plt.plot([0, y_test.max()], [0, y_test.max()], 'r--')  
plt.xlabel('Actual PM10')
plt.ylabel('Predicted PM10')
plt.title('ML Regression: Actual vs Predicted PM10')
plt.savefig('ml_regression_results.png')
print("Saved regression plot to 'ml_regression_results.png'")


#Classification Model

print("\n Classification Model Good vs Poor Air")
# PM10 > 40 is "Poor" else "Good"
threshold = 40
y_class = (y > threshold).astype(int)
y_train_c, y_test_c, X_train_c, X_test_c = train_test_split(y_class, X, test_size=0.2, random_state=42)

classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train_c, y_train_c)

y_pred_class = classifier.predict(X_test_c)

print("Classification Report:")
print(classification_report(y_test_c, y_pred_class, target_names=['Good Air', 'Poor Air']))


# feature analysis

importances = regressor.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
plt.title("What affects Air Quality most?")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), [features[i] for i in indices], rotation=45)
plt.tight_layout()
plt.savefig('ml_feature_importance.png')
