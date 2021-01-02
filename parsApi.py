import requests
import json

def get_Api(url_Api= 'https://www.metaweather.com/api/location/', city='london'):
    city_id = requests.get(url_Api + 'search/?query=' + city).json()[0]['woeid']
    city_5day_forcast_weather = requests.get(url_Api+ str(city_id) + '/').json()
    return city_5day_forcast_weather

def get_date_weatherstatus_tmp_windspeed(forcastjson):
    temp_5day_forcast = []
    weather_status_5day_forcast = []
    wind_speed_5day_forcast = []
    date_5day_forcast = []
    data=[[]]

    for i in range(5):
        temp_5day_forcast.append(round(forcastjson['consolidated_weather'][i + 1]['min_temp'], 2))
        weather_status_5day_forcast.append(forcastjson['consolidated_weather'][i + 1]['weather_state_name'])
        wind_speed_5day_forcast.append(round(forcastjson['consolidated_weather'][i + 1]['wind_speed'], 2))
        date_5day_forcast.append(forcastjson['consolidated_weather'][i + 1]['applicable_date'])
        data.append([date_5day_forcast[i], weather_status_5day_forcast[i], temp_5day_forcast[i], wind_speed_5day_forcast[i]])

    data.pop(0)
    return data

