from kafka import KafkaProducer
from time import sleep
import parsApi
import json

bootstarpServer= ['localhost:9092']

producer = KafkaProducer(bootstrap_servers= bootstarpServer,value_serializer=lambda v: json.dumps(v).encode('utf-8'))

weather_data= parsApi.get_Api(city ='london')

data_weather_forcast_5day= parsApi.get_date_weatherstatus_tmp_windspeed(weather_data)

for e in range(len(data_weather_forcast_5day)):
    temporary_data= data_weather_forcast_5day[e]
    print('done')
    producer.send('weather_forcast', temporary_data)
    sleep(3)

producer.close()
