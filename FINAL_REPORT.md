# Air Quality & Weather Analysis Report
**DSA210 Project - Kadıköy Analysis**

**Data Coverage:** Successfully merged and cleaned 5945 hourly observations from Oct 2024 to Nov 2025.

## 1. Statistical Hypothesis Test
We tested if rain significantly reduces PM10 pollution using a Welch's T-test.
* **Null Hypothesis ($H_0$):** Mean PM10 is the same on rainy vs. dry days.
* **Alternative ($H_1$):** Mean PM10 differs on rainy days.

### Results for PM10:
- **Mean Pollution (Rainy):** 26.47 µg/m³
- **Mean Pollution (Dry):** 33.70 µg/m³
- **P-value:** `1.4222e-44`
> **Conclusion:** The result is **statistically significant** ($p < 0.05$). Rain helps clear the air.

## 2. Visualizations & Exploratory Data Analysis (EDA)
### A. Correlation Matrix
![Correlation Matrix](correlation_matrix.png)
* **Insight:** This heatmap reveals how weather variables interact. A negative correlation between 'Wind Speed' and 'PM10' confirms that wind disperses pollutants.

### B. Scatter Plot (Wind vs. Pollution)
![Scatter Plot](wind_vs_pm10.png)
* **Insight:** The downward trend indicates that higher wind speeds generally result in better air quality.

### C. Time Series Analysis
![Time Series](pm10_timeseries.png)
* **Observation:** We see distinct seasonal spikes. The data covers over a full year, allowing us to see winter vs. summer trends.

### D. Data Distribution Analysis
![Distribution](pm10_distribution.png)
* **Observation:** The data is right-skewed (long tail to the right). Most hours have low pollution, but occasional extreme events occur.
* **Statistical Note:** Although the data is not perfectly normal, the large sample size (N > 5000) allows us to rely on the Central Limit Theorem for our T-test.

### E. Hourly Trends (Rush Hour Effect)
![Hourly Trend](hourly_trend.png)
**Insight into Human Behavior:**
* This plot reveals the impact of human activity vs. nature.
* If spikes are observed around **09:00** and **19:00**, traffic is a likely contributor.
* The lowest values typically occur in the early morning (03:00-05:00), serving as a baseline for background pollution.

