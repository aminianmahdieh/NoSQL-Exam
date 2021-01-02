from kafka import KafkaConsumer
from time import sleep
import json

consumer = KafkaConsumer(
    'weather_forcast',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my forcast',
     value_deserializer=lambda v: json.loads(v.decode('utf-8')))

for msg in consumer:
    array_weather= msg[6]
    print('The weather is predicted for {} to be {}'.format(array_weather[0],array_weather[1]))
    if array_weather[1] == 'Showers':
        print('In the case you want to go out, Do not forget an Umbrella')
    if array_weather[1] == 'Heavy Rain':
        print('In the case you want to go out, Do not forget an Umbrella, Boots and a proper Coat')
    if array_weather[1] == 'Snow':
        print('Well it is snowy you better go out for emergencies or wear proper boot and proper warm cloths')
    if array_weather[1]== 'Sleet':
        print('The weather is messy and dirty today you better take care of your shoes.')
    if array_weather[1]=='Hail':
        print('Wow Wow Wow you can not go out today; It is dangerous.')
    if array_weather[1]== 'Thunders':
        print('You should stay away from windows today.')
    if array_weather[1]== 'Light Rain':
        print('Today can be a romantic day to have a walk with your significant someone around the city.')
    if array_weather[1] =='Heavy Cloud':
        print('There is no promises that it will not turn to a rain, so have your umbrella with your self just in case.')
    if array_weather[1]=='Light Cloud':
        print('The weather is romantic for a good walk around the city.')
    if array_weather[1]=='Clear':
        print('You should go out for picnic today, live this day as you like.')

    if array_weather[2]<0:
        print('!!!Alert!!!!: The weather is too cold; make sure to wear proper warm cloths.')

    if array_weather[3]>10:
        print('The weather is pretty windy')

    print('=============================================================================\n')