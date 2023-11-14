import telebot
import weather

# включение бота
bot = telebot.TeleBot('5454744752:AAFboSLD_pHqFPUXrG_Fup5TVleSker9CXY')
bot.send_message(1899000306, 'i was born')

# прописываем, как будет отвечать, если получил сообщение типа Текст
@bot.message_handler(content_types=['text'])
def message(info):
    # номер чата, куда отвечать
    print(info.chat.id)
    if 'привет' in info.text:
        bot.send_message(info.chat.id, 'hi')
    elif 'пока' in info.text:
        bot.send_message(info.chat.id, 'bye')
    elif 'погода' == info.text:
        pog = weather.weather()
        bot.send_message(info.chat.id, pog)
    elif 'погода на 5 дней' in info.text:
        weather_five = weather.weather_five()
        bot.send_message(info.chat.id, weather_five)
    else:
        bot.send_message(info.chat.id, 'i am a bot')
    pass


bot.polling(none_stop=True, interval=2)
