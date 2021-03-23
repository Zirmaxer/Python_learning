import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru' 
owm = pyowm.OWM('4906af368c1dae3b0457142283e5d764', config_dict )
mgr = owm.weather_manager()

place= input("Введите название города: ")    #Запрос названия города у пользователя

# Search for current weather in town=place and get details
observation = mgr.weather_at_place(place)
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

temp = w.temperature('celsius')["temp"]
clouds = w.detailed_status

print ('В городе ' + str(place) + ' сейчас температура воздуха: ' +str(temp))
print ('На улице: ' + str(clouds))