import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv
load_dotenv()


# gets air quality data from OpenAQ for Kadikoy, Istanbul for 2024-2025 than saves to CSV
API_KEY = os.getenv("API_KEY") 
LOCATION_ID = 3091483          
DATE_FROM = "2024-10-03T00:00:00Z" 
DATE_TO = "2025-11-28T23:59:59Z"


HEADERS = {
    "accept": "application/json",
    "X-API-Key": API_KEY
}

def get_sensor_id(location_id, param_name):
    url = f"https://api.openaq.org/v3/locations/{location_id}"
    try:
        data = requests.get(url, headers=HEADERS).json()
        if 'results' in data and len(data['results']) > 0:
            for sensor in data['results'][0]['sensors']:
                if sensor['parameter']['name'] == param_name:
                    return sensor['id']
    except Exception as e:
        print(f"Error finding sensor: {e}")
    return None

def fetch_hourly_data(sensor_id):
    url = f"https://api.openaq.org/v3/sensors/{sensor_id}/hours"
    params = {
        "datetime_from": DATE_FROM,
        "datetime_to": DATE_TO,
        "limit": 1000,
        "page": 1
    }
    
    all_records = []
    print(f"hourly data for Sensor {sensor_id}")
    
    while True:
        try:
            response = requests.get(url, params=params, headers=HEADERS)
            if response.status_code == 401:
                print("Error: 401 API Key")
                return pd.DataFrame()
            res = response.json()
        except:
            print("Failed. Retrying")
            time.sleep(2)
            continue

        if 'results' not in res or len(res['results']) == 0:
            break
            
        for r in res['results']:
            all_records.append({
                'time': r['period']['datetimeTo']['utc'], 
                'value': r['value']
            })
            
        print(f"     Page {params['page']}: Fetched {len(res['results'])} hours")
        params['page'] += 1
        time.sleep(0.2)
        
    df = pd.DataFrame(all_records)
    if not df.empty:
        df['time'] = pd.to_datetime(df['time'])
        df = df.set_index('time').sort_index()
    return df


print(f"Starting data collection")

id_pm10 = get_sensor_id(LOCATION_ID, 'pm10')
id_pm25 = get_sensor_id(LOCATION_ID, 'pm25')

dfs = []

if id_pm10:
    print(f"Found PM10 Sensor (ID: {id_pm10})")
    df10 = fetch_hourly_data(id_pm10).rename(columns={'value': 'pm10'})
    if not df10.empty: dfs.append(df10)

if id_pm25:
    print(f"Found PM2.5 Sensor (ID: {id_pm25})")
    df25 = fetch_hourly_data(id_pm25).rename(columns={'value': 'pm25'})
    if not df25.empty: dfs.append(df25)

if not dfs:
    print("No data found")
else:
    aq_df = dfs[0]
    if len(dfs) > 1:
        aq_df = pd.merge(dfs[0], dfs[1], left_index=True, right_index=True, how='outer')

  
    aq_df.to_csv('kadikoy_air_quality_2024_2025.csv')
    print(f"Saved {len(aq_df)} rows to 'kadikoy_air_quality_2024_2025.csv'")