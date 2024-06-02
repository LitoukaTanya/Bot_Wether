import telebot
import requests
import json

bot = telebot.TeleBot('7427076272:AAHT0Ln3AzVxs2zRnmH7C2R7W5fY741cy1Y')
API = "1495b3fc5ef5adfd1b4820b499ba632a"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет {message.chat.first_name}, напиши в каком городе тебя интересует погода")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message, f"Погода в городе {city} сейчас: {data['main']['temp']}")


bot.polling(non_stop=True)
