import telebot
import requests
import json

bot = telebot.TeleBot('7427076272:AAHT0Ln3AzVxs2zRnmH7C2R7W5fY741cy1Y')
API = "1495b3fc5ef5adfd1b4820b499ba632a"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}! 👋\n\n"
        "Я погодный бот. 🌤️ Напиши мне название города, и я скажу тебе текущую погоду в этом месте. ")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f"Погода в городе {city} сейчас: {data['main']['temp']}")

    else:
        bot.send_message(message.chat.id, "Неверно указан город")


bot.polling(non_stop=True)
