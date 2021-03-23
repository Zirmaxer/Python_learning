import telebot
import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru' 
owm = pyowm.OWM('4906af368c1dae3b0457142283e5d764', config_dict )
mgr = owm.weather_manager()
bot = telebot.TeleBot("1532359746:AAHVxk35oLr8rYnIewp4Pl32HJr_tiYGjoM", parse_mode=None) 

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
	#bot.send_message( message.chat.id, message.text )
	observation = mgr.weather_at_place( message.text )
	w = observation.weather
	temp = w.temperature('celsius')["temp"]
	clouds = w.detailed_status

	answer =('В городе ' + message.text + ' сейчас температура воздуха: ' +str(temp) +"\n")
	answer += ('На улице: ' + str(clouds) +"\n\n")
	bot.send_message( message.chat.id, answer )

bot.polling( none_stop=True )