# Air Quality & Weather Analysis: Kadıköy, Istanbul
**DSA210 Term Project Mustafa Ata Yılmaz**

## 1. Project Overview
This project analyzes the relationship between meteorological conditions and air quality in the Kadıköy district of Istanbul, Turkey **from October 2024 to November 2025**. As an industrial megacity, Istanbul frequently experiences poor air quality events. This analysis focuses on how weather patterns specifically precipitation, wind speed, and human behavior like rush hours impact Particulate Matter (PM10) concentrations.

**Key Objective:** Key Objective: To statistically validate the "Washout Effect" (rain cleaning the air) and the "Ventilation Effect" (wind dispersing pollutants), while identifying pollution trends driven by urban activity.

## 2. Data Sources
This project combines two distinct datasets covering the period from **October 2024 to November 2025**.

### A. Air Quality Data
* **Source:** [OpenAQ API](https://openaq.org/) (Aggregates data from the Turkish National Air Quality Monitoring Network).
* **Metric:** PM10 (Particulate Matter < 10 micrometers).
* **Collection:** Fetched via `fetch_air_quality.py` using the Kadıköy Sensor ID (`3091483`).

### B. Weather Data
* **Source:** [Meteostat](https://meteostat.net/).
* **Metrics:** Temperature (°C), Humidity (%), Precipitation (mm), Wind Speed (km/h).
* **Collection:** Fetched via `fetch_weather.py` using geospatial coordinates for Kadıköy (40.990, 29.025).

**Data Processing:** The datasets were merged on hourly timestamps, resulting in **5,945 clean hourly observations** for analysis.

## 3. Methodology & Analysis
The analysis pipeline involves data cleaning, merging, visualization, and hypothesis testing using Python.

### Statistical Hypothesis Test
We conducted a **Welch’s T-test** to determine if rain significantly reduces PM10 levels.
* **Null Hypothesis ($H_0$):** Mean PM10 is the same on rainy vs. dry days.
* **Result:** The analysis yielded a P-value of `1.42e-44`, effectively rejecting the null hypothesis.
* **Finding:** Rain reduces PM10 concentrations by approximately **21.5%** (a drop of ~7.23 µg/m³), confirming a strong washout effect.


### Exploratory Data Analysis (EDA)
* **Correlation Analysis:** Found a negative correlation between Wind Speed and PM10 ($r \approx -0.15$), indicating that stagnant air leads to pollution buildup.
* **Human Behavior:** Hourly analysis revealed a distinct **"M-shaped" pattern** with peaks at **09:00** and **17:00**, correlating perfectly with Istanbul's morning and evening rush hours.
* **Thresholds:** Pollution events (>100 µg/m³) were found to occur almost exclusively when wind speeds dropped below 10 km/h.

## 4. Machine Learning Analysis
To predict Air Quality (PM10) based on weather conditions, we implemented a **Random Forest Regressor** and a **Classifier**.

### Model Performance
* **Regression (Predicting exact PM10 value):**
    * **R² Score:** `0.86` (The model explains 86% of the variance in air quality).
    * **MAE:** `3.97 µg/m³` (Average prediction error).
    * *Result:* The high R² score confirms that air quality is highly predictable using weather data and time features.
* **Classification (Predicting "Good" vs "Poor" Air):**
    * **Accuracy:** `93%`
    * **Recall for Poor Air:** `0.87` (The model successfully detects 87% of pollution spikes).

### Feature Importance
The Random Forest model identified which factors drive pollution most significantly:
1.  **Temperature:** The strongest predictor (likely due to seasonal inversions).
2.  **Month & Time:** Human behavioral cycles are the second most important factor.
3.  **Wind Speed:** Confirms the "Ventilation Effect" hypothesis.

![Feature Importance](images/ml_feature_importance.png)

### Prediction Visualization
The scatter plot below shows the Actual vs. Predicted PM10 levels. The tight clustering around the red line indicates strong model performance.

![Regression Results](images/ml_regression_results.png)
## 5. How to Run

This project is structured into three modular scripts: two for data collection and one for analysis. Follow the steps below to reproduce the results.

### 1. Prerequisites
Install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
````

### 2\. API Configuration

The air quality data is fetched from OpenAQ, which requires an API key.

1.  Obtain a API key from [OpenAQ](https://openaq.org/).

3.  Create and add your key to the .env file in the following format:
    ```text
    API_KEY=your_key
    ```

### 3\. Data Collection

Run the fetch scripts to download the raw data. These will generate local CSV files covering the period from Oct 2024 to Nov 2025.

  * **Get Weather Data:**

    ```bash
    python fetch_weather.py
    ```

    *Output:* `kadikoy_weather_2024_2025.csv` (Temperature, Wind, Precipitation)

  * **Get Air Quality Data:**

    ```bash
    python fetch_air_quality.py
    ```

    *Output:* `kadikoy_air_quality_2024_2025.csv` (PM10, PM2.5)

### 4\. Analysis & Report Generation
Run the main analysis script for statistical tests and the ML script for predictive modeling.

```bash
python main_analysis.py
python ml_analysis.py
```
### 5\. Expected Output

After running the analysis, the following files will be generated in your project folder:

  * **REPORT.md:** A comprehensive summary of findings and hypothesis test results.
  * **data_relations.csv:** The correlation matrix of the merged dataset.
  * **Visualizations (PNG):**
      * **correlation_matrix.png**
      * **wind_vs_pm10.png**
      * **pm10_timeseries.png**
      * **pm10_distribution.png**
      * **hourly_trend.png**
      * **ml_regression_results.png**
      * **ml_feature_importance.png**

## 6. Limitations
* **Limitation:** The dataset currently covers only one district (Kadıköy). Results might not generalize to the European side of Istanbul.
* **Limitation:** We used a standard Random Forest. Deep Learning (LSTM) might better capture time-series dependencies.
