# Predicting Air Quality In Industrial Areas Using Meteorological data
Project for Dsa210 class by Mustafa Ata Yılmaz

## 1. Project proposal:

The goal for this project is to analyze how weather patterns affects air quality in Istanbul, Turkey. This data may prove to be a valuable tool for health and insurance organizations. As an industrial megacity, Istanbul, frequently experiences poor air quality events.These events are often strongly influenced by meteorological factors like wind speed, humidity, and temperature inversions, which can trap or disperse airborn pollutants.

## 2. Data Source 

This project will combine two datasets, Base Dataset:Historical Air Quality Data for Istanbul 
Source: https://openaq.org/ which aggregates data from the Turkish National Air Quality Monitoring Network (Ulusal Hava Kalitesi İzleme Ağı).

Collection Plan: I am planning on using the openaq Python library to query the API for historical hourly data for the full year of 2024 (Jan 1 - Dec 31).  The data will include key pollutants, specifically PM10 and PM2.5.

Second Dataset: Historical Weather Data for Istanbul
Collection Plan: For the same time period (2024), I will use the meteostat Python library to download historical hourly weather data from a nearby weather station. The data will include: Temprature in C, relative humidity as a percentage, precipitation in mm, average wind speed in km/h and wind direction in degrees.

Combining the datasets: : Both datasets will be loaded into pandas, resampled to a consistent hourly frequency, and then merged into a single DataFrame using their timestamp as the primary key.

## 3. Analysis and Methodology

Data Cleaning: The merged data will be cleaned to problematic values. I will conduct exploratory  data analysis to find initial correlations, creating time series plots to observe seasonal pollution trends and scatter plots to visualize the relationship between wind speed and PM10.

Hypothesis Test: I will conduct a t-test to validate the hypothesis that the mean PM10 concentration on rainy days (precipitation > 0) is significantly lower than on dry days.

## 4. Appling ML methods on the dataset

Method: I am planning to frame this as a regression problem.
Target Variable: PM10 value 24 hours in the future.
Features: Will include all weather data, time based features, and air quality metrics.

Models: I am planning to start with a Linear Regression model as a baseline, then implement and compare its performance against a Random Forest Regressor or Gradient Boosting to capture more complex relationships.